from flask import Flask, request
from typing import Optional
from pydantic import BaseModel, ValidationError


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return {"response": "Hello, World!"}

    return app
