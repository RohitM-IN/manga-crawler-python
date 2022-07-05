from flask import Flask, jsonify
from utils.cleaner import response
import sys

app = Flask(__name__)

from src.blueprints.asurascans import asurascans

app.register_blueprint(asurascans, url_prefix='/api/v1/')

@app.route('/')
def index():
    return response("Hello, World!")