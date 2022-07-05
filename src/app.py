from flask import Flask, jsonify
import sys

app = Flask(__name__)

from src.blueprints.asurascans import asurascans

app.register_blueprint(asurascans)

@app.route('/')
def index():
    return "Hello, World!"