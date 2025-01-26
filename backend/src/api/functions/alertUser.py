import math

import configparser

from api.database.models import User
from api.functions.alerts import send_alerts
from api.database.models import db

# Config setup
config = configparser.ConfigParser()
config.read("../backend/disaster_radius.conf")


def is_within_radius(
    lat1: float, lon1: float, lat2: float, lon2: float, radius_km: float
) -> bool:
    """
    Determine if the point (lat2, lon2) is within the radius_km of the point (lat1, lon1).

    Args:
        lat1 (float): Latitude of the center point.
        lon1 (float): Longitude of the center point.
        lat2 (float): Latitude of the point to check.
        lon2 (float): Longitude of the point to check.
        radius_km (float): Radius in kilometers.

    Returns:
        bool: True if the point is within the radius, False otherwise.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance_km = R * c

    return distance_km <= radius_km


def calculate_radius_bound(lat: float, lon: float, radius_km: float):
    """
    Calculate the bounding box around a point (lat, lon) with a given radius in kilometers.

    Args:
        lat (float): Latitude of the center point.
        lon (float): Longitude of the center point.
        radius_km (float): Radius in kilometers.

    Returns:
        tuple: A tuple containing the minimum latitude, maximum latitude, minimum longitude, and maximum longitude.
    """
    # Earth's radius in kilometers
    R = 6371.0

    # Latitude and longitude in radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Radius in radians
    radius_rad = radius_km / R

    # Bounding box
    min_lat = lat_rad - radius_rad
    max_lat = lat_rad + radius_rad
    min_lon = lon_rad - radius_rad / math.cos(lat_rad)
    max_lon = lon_rad + radius_rad / math.cos(lat_rad)

    # Convert back to degrees
    return (
        math.degrees(min_lat),
        math.degrees(max_lat),
        math.degrees(min_lon),
        math.degrees(max_lon),
    )


def notify_users_within_radius(disaster: dict, app):
    """_summary_

    Args:
        lat (float): _description_
        lon (float): _description_
        disaster_type (str): _description_
    """
    SUBJECT = "A NEW ALERT IN YOUR AREA"

    disaster_lat = disaster.get("lat")
    disaster_lon = disaster.get("long")
    disaster_type = disaster.get("type")
    disaster_time = disaster.get("time")

    message = "IMPORTANT MESSAGE WILL FOLLOW BELLOW\n"
    message += f"Disaster Type: {disaster_type}\n"
    message += f"Report Time: {disaster_time}\n\n"
    message += f"Please visit the following resources for help.\n\n"

    radius_km = float(config["DISASTER"][disaster_type].replace("km", ""))
    emergency_contact = config["DISASTER"][f"{disaster_type}_Resource"]
    emergency_contact = emergency_contact.replace("\\n", "\n")
    message += emergency_contact
    message += "\n\nCALL 911 IF YOU NEED IMMEDIATE ASSISTANCE"

    min_lat, max_lat, min_lon, max_lon = calculate_radius_bound(
        disaster_lat, disaster_lon, radius_km
    )

    with app.app_context():
        try:
            users = (
                db.session.query(User)
                .filter(
                    User.lat.between(min_lat, max_lat),
                    User.long.between(min_lon, max_lon),
                )
                .all()
            )

            print(f"Found {len(users)} users within the radius.")

            for user in users:
                if is_within_radius(
                    disaster_lat, disaster_lon, user.lat, user.long, radius_km
                ):
                    try:
                        send_alerts(
                            subject=SUBJECT,
                            body=message,
                            email_address=user.email,
                            phone_number=user.phone,
                        )
                    except Exception as e:
                        print(f"Error sending alert to user {user.id}: {e}")
        finally:
            db.session.close()
