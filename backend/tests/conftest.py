# Conftest.py is a file that contains fixtures that are shared across multiple test files
import pytest
from backend.app import create_app
from backend.database.models import db


# Use this fixture to do interactions with the app
@pytest.fixture()
def app():
    # Put setup code here (instead of doing this, could create a create_app factory to add config)
    yield create_app()
    # Put teardown code here


# Use this fixture to pretend to be a client making GET and POST requests
@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def clear_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_examples()
