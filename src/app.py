from flask import Flask
from utils.utils import response
from utils.cache import cache
from config import CONFIG, FRESH_PROXY_REFESH_INTERVAL
from flask_apscheduler import APScheduler
from proxy.proxy import getProxy


app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config.from_mapping(CONFIG)
cache.init_app(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(id = 'Fresh Proxy', func=getProxy, trigger="interval", seconds=FRESH_PROXY_REFESH_INTERVAL)
scheduler.start()


from src.blueprints.asurascans import asurascans
from src.blueprints.reaperscans import reaperscans
from src.blueprints.flamescans import flamescans
# from src.blueprints.errors import errors

# app.register_blueprint(errors)
app.register_blueprint(asurascans, url_prefix='/api/v1/asura')
app.register_blueprint(reaperscans, url_prefix='/api/v1/reaper')
app.register_blueprint(flamescans, url_prefix='/api/v1/flame')
# TODO: make dragontea.ink blueprint


@app.route('/')
def index():
    return response("Pong")