from pydantic import BaseModel
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


class UserSchema(BaseModel):
    """A schema to validate when creating a user."""

    lat: float
    long: float
