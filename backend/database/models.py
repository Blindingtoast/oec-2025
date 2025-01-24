from pydantic import BaseModel
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Report(db.Model):
    """A report of an incident."""

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, lat: float, long: float, type: str, time: str, description: str):
        """Initialize a report

        Args:
            lat (float): latitude in degrees
            long (float): longitude in degrees
            type (str): type of report
            time (str): the time in ISO format
            description (str): a description of the report
        """
        self.lat = lat
        self.long = long
        self.type = type
        self.time = datetime.fromisoformat(time)
        self.description = description

    def to_dict(self):
        """Convert the report to a dictionary.

        Returns: The report as a dictionary.
            _type_: dict
        """
        return {
            "id": self.id,
            "lat": self.lat,
            "long": self.long,
            "type": self.type,
            "time": self.time.isoformat(),
            "description": self.description,
        }


class ReportSchema(BaseModel):
    """A schema to validate when creating a report."""

    lat: float
    long: float
    type: str
    time: str
    description: str


class User(db.Model):
    """A user of the application who wants to receive reports."""

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)


class UserSchema(BaseModel):
    """A schema to validate when creating a user."""

    lat: float
    long: float
    email: str
    phone: str


class UserNotification(db.Model):
    """Instances of users receiving notifications. Used to ensure that a user
    does not receive multiple notifications at the same time."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    disaster_type = db.Column(db.String(50), nullable=False)
    notification_time = db.Column(db.DateTime, nullable=False)
