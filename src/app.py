from flask import Flask, jsonify
from utils.cleaner import response
from werkzeug import exceptions
from utils.cache import cache
import sys

config = {
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config.from_mapping(config)
cache.init_app(app)


from src.blueprints.asurascans import asurascans
from src.blueprints.errors import errors

app.register_blueprint(errors)
app.register_blueprint(asurascans, url_prefix='/api/v1/')


@app.route('/')
def index():
    return response("Hello, World!")