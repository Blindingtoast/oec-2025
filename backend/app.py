from flask import Flask, request
from backend.database.examples import create_examples
from backend.database.models import db
from backend.api import api
import os


def create_app():
    """Create a Flask application instance.

    Returns: The Flask app instance.
        _type_: Flask
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    create_db(app)

    @app.route("/")
    def hello_world():
        return {"response": "Hello, World!"}

    app.register_blueprint(api)

    return app


def create_db(app: Flask):
    """Create the database tables using SQLite.

    Args:
        app: The Flask application instance.
            _type_: Flask
    """
    exists = os.path.exists(
        os.path.join(os.path.dirname(__file__), "instance", "database.db")
    )
    db.init_app(app)
    with app.app_context():
        db.create_all()
        if not exists:
            create_examples()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
