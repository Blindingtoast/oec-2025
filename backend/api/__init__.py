from flask import Blueprint

from api.reports import reports
from api.users import users

api = Blueprint("api", __name__)

api.register_blueprint(reports)
api.register_blueprint(users)
