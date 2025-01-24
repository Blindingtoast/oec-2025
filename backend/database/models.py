from pydantic import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Report(db.Model):
    """A report of an incident.

    Args:
        db (_type_): The SQLAlchemy database instance.
    """

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(500), nullable=False)

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
    """A schema to validate when creating a report.

    Args:
        BaseModel (_type_): The Pydantic base model.
    """

    lat: float
    long: float
    type: str
    time: str
    description: str


class User(db.Model):
    """A user of the application who wants to receive reports.

    Args:
        db (_type_): The SQLAlchemy database instance.
    """

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)


class UserSchema(BaseModel):
    """A schema to validate when creating a user.

    Args:
        BaseModel (_type_): The Pydantic base model.
    """

    lat: float
    long: float
