from flask import Blueprint

from api.routes.reports import reports
from api.routes.users import users

api_bp = Blueprint("api", __name__)

api_bp.register_blueprint(reports)
api_bp.register_blueprint(users)
