from flask import Blueprint, jsonify, request, Response
from pydantic import ValidationError

from backend.database.models import db, User, UserSchema

users = Blueprint("users", __name__)


@users.route("/users/notifyme", methods=["POST"])
def notify_user():
    """Subscribe a user to receive notifications.

    Returns: A JSON response.
        _type_: Response
    """
    data = request.get_json()
    try:
        UserSchema(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()})

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"response": "User will be updated."})
