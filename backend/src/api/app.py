import os

from flask import Flask
from flask_sock import Sock

from api.database.examples import create_examples
from api.database.models import db, Report, User
from api.routes import api_bp
from api.functions.alerts import setup_env
from api.updates.reports import setup_sock


def create_app(config_name: str = "default") -> Flask:
    """Create a Flask application instance."""
    app = Flask(__name__)
    app.register_blueprint(api_bp)

    if config_name == "testing":
        # So that testing data does not persist
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TWILIO"] = False
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
        # Set TWILIO to false if it shouldn't be used
        app.config["TWILIO"] = setup_env()

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    create_db(app)
    setup_sock(app)
    return app


def db_path(app: Flask):
    return os.path.join(app.instance_path, "database.db")


def create_db(app: Flask):
    """Create the database tables using SQLite.

    Args:
        app: The Flask application instance.
            _type_: Flask
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
        if not os.path.exists(db_path(app)):
            create_examples()


def clear_db(app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
