from flask import Flask, jsonify
from utils.utils import response
from werkzeug import exceptions
from utils.cache import cache
import sys
from config import CACHE_TIME

config = {
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": CACHE_TIME
}

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config.from_mapping(config)
cache.init_app(app)


from src.blueprints.asurascans import asurascans
from src.blueprints.reaperscans import reaperscans
from src.blueprints.errors import errors

app.register_blueprint(errors)
app.register_blueprint(asurascans, url_prefix='/api/v1/asura')
app.register_blueprint(reaperscans, url_prefix='/api/v1/reaper')


@app.route('/')
def index():
    return response("Hello, World!")