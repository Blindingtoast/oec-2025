from flask import Blueprint, jsonify, request, Response
from pydantic import ValidationError

from database.models import db, Report, ReportSchema

reports = Blueprint("reports", __name__)


@reports.route("/reports/create", methods=["POST"])
def create_report():
    """Create a new report.

    Returns: A JSON response.
        _type_: Response
    """
    data = request.get_json()
    try:
        ReportSchema(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()})
    report = Report(**data)
    db.session.add(report)
    db.session.commit()
    return jsonify({"response": "Report created."})


@reports.route("/reports/modify", methods=["POST"])
def modify_report():
    """Modify an existing report.

    Returns: A JSON response.
        _type_: Response
    """
    data = request.get_json()
    try:
        ReportSchema(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()})

    report = Report.query.get(data["id"])
    if not report:
        return jsonify({"error": "Report not found."})
    report.lat = data["lat"]
    report.long = data["long"]
    report.type = data["type"]
    report.time = data["time"]
    report.description = data["description"]
    db.session.commit()
    return jsonify({"response": "Report modified."})


@reports.route("/reports/delete", methods=["POST"])
def delete_report():
    """Delete an existing report.

    Returns: A JSON response.
        _type_: Response
    """
    data = request.get_json()
    report = Report.query.get(data["id"])
    if not report:
        return jsonify({"error": "Report not found."})
    db.session.delete(report)
    db.session.commit()
    return jsonify({"response": "Report deleted."})


@reports.route("/reports/locations", methods=["GET"])
def get_locations():
    """Get all the report locations.

    Returns: A JSON response.
        _type_: Response
    """
    reports = Report.query.all()
    locations = [report.to_dict() for report in reports]
    return jsonify(locations)
