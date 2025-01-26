import os
from flask import Flask, request

from database.examples import create_examples
from database.models import db, Report, User
from routes import api_bp
from functions.alerts import setup_env


def create_app(config_name: str = "default") -> Flask:
    """Create a Flask application instance.

    Returns: The Flask app instance.
        _type_: Flask
    """
    app = Flask(__name__)
    app.register_blueprint(api)

    if config_name == "testing":
        # So that testing data does not persist
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TWILIO"] = False
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
        # Set TWILIO to false if it shouldn't be used
        app.config["TWILIO"] = setup_env()
        app.logger.info(f"app twilio is enabled: {app.config['TWILIO']}")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    create_db(app)
    return app


def create_db(app: Flask):
    """Create the database tables using SQLite.

    Args:
        app: The Flask application instance.
            _type_: Flask
    """
    exists = os.path.exists(
        os.path.join(os.path.dirname(__file__), "instance/database.db")
    )
    db.init_app(app)
    with app.app_context():
        db.create_all()
        if not exists:
            create_examples()


def clear_db(app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
