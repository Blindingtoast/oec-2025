import time
from datetime import datetime

from flask_sock import Sock
from flask import current_app
from pydantic import BaseModel

from api.database.models import db, Report, ReportSchema


class ReportUpdate(BaseModel):
    reports: list[ReportSchema]
    time: datetime


# Needs to be initialized in the main app
sock: Sock = Sock()

UPDATE_INTERVAL = 5


def get_updates(since: datetime) -> ReportUpdate:
    """Get all updates since the given time."""
    updates = db.session.query(Report).filter(Report.time >= since).all()
    current_app.logger.info("got some updates to send: " + str(updates))
    return ReportUpdate(reports=updates, time=datetime.now())


def setup_sock(app):
    sock = Sock(app)

    @sock.route("/updates/test")
    def test(sock):
        while True:
            data = sock.receive()
            current_app.logger.info(f"received: {data}")
            sock.send(data)

    @sock.route("/updates/reports")
    def route_updates(sock):
        current_app.logger.info("websocket connected")
        while True:
            now = datetime.now()
            time.sleep(UPDATE_INTERVAL)
            updates = get_updates(now)
            if updates:
                sock.send(updates.model_dump_json())
            else:
                sock.send("no updates")
