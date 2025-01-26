import random
import datetime
from api.database.models import ReportSchema, UserSchema


def generate_report(lat, lon, deviation, types):
    """Create a report to be sent by a client, with a random name

    Args:
        lat (float): a latitude coordinate
        lon (float): a longitude coordinate
        radius (float): the distance (in kilometers) from the coordinates that a report can be generated
        type (list[ReportType]): the types of reports that can be generated
    """
    # Conver deviation from km to degrees
    deg_dev = deviation / 111.0
    rand_lat = random.gauss(lat, deg_dev)
    rand_lon = random.gauss(lon, deg_dev)
    reporttime = datetime.datetime.now().isoformat()
    report = ReportSchema(
        lat=rand_lat,
        long=rand_lon,
        type=random.choice(types),
        time=reporttime,
        description="This is a test report",
    )
    return report


def generate_user(lat, lon, deviation):
    rand_lat = random.gauss(lat, deviation)
    rand_lon = random.gauss(lon, deviation)
    email = "testemail@email.com"
    phone = "123-456-7890"
    user = UserSchema(lat=rand_lat, long=rand_lon, email=email, phone=phone)
    return user
