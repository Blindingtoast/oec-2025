from database.models import db, Report, User
from datetime import datetime


def create_report(lat: float, long: float, type: str, time: str, description: str):
    """Create a new report in the database.

    Args:
        lat: The latitude of the report.
            _type_: float
        long: The longitude of the report.
            _type_: float
        type: The type of the report.
            _type_: str
        time: The time of the report.
            _type_: str
        description: The description of the report.
            _type_: str
    """
    report = Report(
        lat=lat,
        long=long,
        type=type,
        time=time,
        description=description,
    )
    db.session.add(report)
    db.session.commit()


def create_user(lat: float, long: float, email: str | None, phone: str | None):
    """Create a new user in the database.

    Args:
        lat: The latitude of the user.
            _type_: float
        long: The longitude of the user.
            _type_: float
        email: The email of the user.
            _type_: str
        phone: The phone number of the user.
            _type_: str
    """
    user = User(lat=lat, long=long, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()


def create_example_reports():
    """Create example reports in the database."""
    reports = [
        (
            50.192562,
            -126.071403,
            "Fire",
            "2021-01-01T12:00:00",
            "There is a fire in Toronto.",
        ),
        (
            49.372327,
            -122.971205,
            "Flood",
            "2021-01-01T12:00:00",
            "There is a flood in Ottawa.",
        ),
        (
            53.452704,
            -113.391127,
            "Earthquake",
            "2021-01-01T12:00:00",
            "There is an earthquake in Winnipeg.",
        ),
        (
            49.941291,
            -97.438979,
            "Tornado",
            "2021-01-01T12:00:00",
            "There is a tornado in Edmonton.",
        ),
        (
            43.791682,
            -79.465346,
            "Blizzard",
            "2021-01-01T12:00:00",
            "There is a blizzard in Thunder Bay.",
        ),
        (
            43.350854,
            -79.953518,
            "Hurricane",
            "2021-01-01T12:00:00",
            "There is a hurricane in Quebec City.",
        ),
        (
            44.281493,
            -76.451239,
            "Tsunami",
            "2021-01-01T12:00:00",
            "There is a tsunami in Halifax.",
        ),
        (
            45.386073,
            -75.736893,
            "Avalanche",
            "2021-01-01T12:00:00",
            "There is an avalanche in Prince George.",
        ),
        (
            48.042415,
            -77.779777,
            "Drought",
            "2021-01-01T12:00:00",
            "There is a drought in St. John's.",
        ),
        (
            58.731534,
            -94.153005,
            "Wildfire",
            "2021-01-01T12:00:00",
            "There is a wildfire in Saskatoon.",
        ),
        (
            61.128773,
            -94.173439,
            "Storm",
            "2021-01-01T12:00:00",
            "There is a storm in Churchill.",
        ),
        (
            45.634985,
            -73.703588,
            "Heatwave",
            "2021-01-01T12:00:00",
            "There is a heatwave in Montreal.",
        ),
        (
            47.730929,
            -58.486207,
            "Cold Snap",
            "2021-01-01T12:00:00",
            "There is a cold snap in Corner Brook.",
        ),
    ]
    for report in reports:
        create_report(*report)


def create_user_examples():
    """Create example users in the database."""
    users = [
        (43.239563, -79.885557, "blindingtoast3@gmail.com", "+12897757139"),
        (43.242927, -79.897079, "btran0820003@gmail.com", "+16138544327"),
    ]
    for user in users:
        create_user(*user)


def create_examples():
    """Create example reports and users in the database."""
    print("Creating example reports and users.")
    create_example_reports()
    create_user_examples()
