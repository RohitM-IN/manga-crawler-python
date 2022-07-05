from flask import Flask, jsonify
from utils.cleaner import response
from werkzeug import exceptions
import sys

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

from src.blueprints.asurascans import asurascans
from src.blueprints.errors import errors

app.register_blueprint(errors)
app.register_blueprint(asurascans, url_prefix='/api/v1/')


@app.route('/')
def index():
    return response("Hello, World!")