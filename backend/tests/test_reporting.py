from backend.database.models import User, Report, db
from backend.tests.utils import generate_user, generate_report
import time
import logging

logger = logging.getLogger(__name__)

TEST_TYPES = ["fire", "flood", "earthquake", "tornado", "hurricane"]


def test_add_single_user(client, empty_db):
    """Test adding a single user"""
    user = generate_user(0, 0, 10)

    # A dict with the different fields in the request body we need
    response = client.post(
        "/users/notifyme", json=user.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added = db.session.query(User).filter_by(lat=user.lat, long=user.long).first()
    assert added is not None, "user was not added"


def test_single_report(client, empty_db):
    """Test adding a single report"""
    report = generate_report(0, 0, 10, TEST_TYPES)

    response = client.post(
        "/reports/create", json=report.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added = (
        db.session.query(Report)
        .filter_by(
            lat=report.lat,
            long=report.long,
        )
        .first()
    )
    assert added is not None, "report not added"


def test_multiple_reports(client, empty_db):
    """Test adding multiple reports"""
    reports = [generate_report(0, 0, 10, TEST_TYPES) for _ in range(20)]

    for report in reports:
        response = client.post(
            "/reports/create", json=report.model_dump(), content_type="application/json"
        )
        assert (
            response.status_code == 200
        ), f"Unexpected status code: {response.status_code}"

    added_reports = db.session.query(Report).all()
    assert len(added_reports) == 20, "Not all reports were added"


def test_reports_over_time(client, empty_db):
    """Test creating reports over multiple seconds"""
    start_time = time.time()
    reports = []
    TEST_DURATION = 3

    logger.info(f"Creating tests over {TEST_DURATION} seconds")
    while time.time() - start_time < TEST_DURATION:
        report = generate_report(0, 0, 10, TEST_TYPES)
        reports.append(report)
        response = client.post(
            "/reports/create", json=report.model_dump(), content_type="application/json"
        )
        assert (
            response.status_code == 200
        ), f"Unexpected status code: {response.status_code}"
        time.sleep(0.5)  # Create a report every 0.5 seconds

    added_reports = db.session.query(Report).all()
    assert len(added_reports) == len(reports), "Not all reports were added"


def test_modify_report(client, empty_db):
    """Test modifying an existing report"""
    report = generate_report(0, 0, 10, TEST_TYPES)
    response = client.post(
        "/reports/create", json=report.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added_report = (
        db.session.query(Report).filter_by(lat=report.lat, long=report.long).first()
    )
    assert added_report is not None, "report not added"

    modified_data = {
        "id": added_report.id,
        "lat": report.lat + 1,
        "long": report.long + 1,
        "type": "modified_type",
        "time": report.time,
        "description": "This is a modified test report",
    }

    response = client.post(
        "/reports/modify", json=modified_data, content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    modified_report = db.session.query(Report).filter_by(id=added_report.id).first()
    assert modified_report.lat == modified_data["lat"], "report latitude not modified"
    assert (
        modified_report.long == modified_data["long"]
    ), "report longitude not modified"
    assert modified_report.type == modified_data["type"], "report type not modified"
    assert (
        modified_report.description == modified_data["description"]
    ), "report description not modified"


def test_delete_report(client, empty_db):
    """Test deleting an existing report"""
    report = generate_report(0, 0, 10, TEST_TYPES)
    response = client.post(
        "/reports/create", json=report.model_dump(), content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    added_report = (
        db.session.query(Report).filter_by(lat=report.lat, long=report.long).first()
    )
    assert added_report is not None, "report not added"

    delete_data = {"id": added_report.id}

    response = client.post(
        "/reports/delete", json=delete_data, content_type="application/json"
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    deleted_report = db.session.query(Report).filter_by(id=added_report.id).first()
    assert deleted_report is None, "report not deleted"


def test_get_locations(client, empty_db):
    """Test fetching all report locations"""
    reports = [generate_report(0, 0, 10, TEST_TYPES) for _ in range(5)]

    for report in reports:
        response = client.post(
            "/reports/create", json=report.model_dump(), content_type="application/json"
        )
        assert (
            response.status_code == 200
        ), f"Unexpected status code: {response.status_code}"

    response = client.get("/reports/locations")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    locations = response.get_json()
    assert len(locations) == 5, "Not all report locations were fetched"
