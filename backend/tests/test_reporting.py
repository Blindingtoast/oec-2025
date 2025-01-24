import pytest
from backend.database.models import UserSchema, ReportSchema, User, Report, db
import random
import datetime


TEST_TYPES = ["fire", "flood", "earthquake", "tornado", "hurricane"]


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
    user = UserSchema(lat=rand_lat, long=rand_lon)
    return user


def test_add_single_user(client, empty_db):
    user = generate_user(0, 0, 10)

    # A dict with the different fields in the request body we need
    response = client.post(
        "/users/notifyme", json=user.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added = db.session.query(User).filter_by(lat=user.lat, long=user.long).first()
    assert added is not None, "user was not added"


def test_single_report(client, empty_db):
    report = generate_report(0, 0, 10, TEST_TYPES)

    response = client.post(
        "/reports/create", json=report.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added = (
        db.session.query(Report)
        .filter_by(
            lat=report.lat,
            long=report.long,
        )
        .first()
    )
    assert added is not None, "report not added"
