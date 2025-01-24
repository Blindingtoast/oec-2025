# Conftest.py is a file that contains fixtures that are shared across multiple test files
import pytest
from backend.app import create_app, clear_db
from backend.database.models import db


# Use this fixture to do interactions with the app
@pytest.fixture()
def app():
    # Put setup code here (instead of doing this, could create a create_app factory to add config)
    app = create_app(config_name="testing")
    with app.app_context():
        yield app
    # Put teardown code here


# Use this fixture to pretend to be a client making GET and POST requests
@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def empty_db(app):
    clear_db(app)
