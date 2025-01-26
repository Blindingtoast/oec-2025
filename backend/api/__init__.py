from flask import Blueprint

from backend.api.reports import reports
from backend.api.users import users

api = Blueprint("api", __name__)

api.register_blueprint(reports)
api.register_blueprint(users)
