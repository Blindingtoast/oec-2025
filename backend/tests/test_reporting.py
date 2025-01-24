import pytest
from backend.database.models import UserSchema, ReportSchema, db
import random
import datetime


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
    reporttime = datetime.datetime.now().iosformat()
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


def test_add_single_user(client, clear_db):
    user = generate_user(0, 0, 10)

    added = db.session.query.filter_by(lat=user.lat, long=user.long).first()
    assert added is not None, "user was not added"
    # A dict with the different fields in the request body we need
    client.post("/users", data=user.model_dump())


def test_single_report(client, clear_db):
    report = generate_report()

    added = db.session.query.filter_by(lat=report.lat, long=report.long,).first()
    client.post("/reports", data=report.model_dump())
