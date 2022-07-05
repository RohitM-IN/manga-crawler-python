from flask import Blueprint, jsonify, request, abort
from utils.cleaner import reaper
from werkzeug.exceptions import BadRequest
from utils.cache import cache
from utils.utils import response, make_error

reaperscans = Blueprint(name="Reaper", import_name=__name__)

@reaperscans.route("/", methods=["GET"])
@cache.cached(timeout=50)
def getList():
    data = []
    count = 0
    while True:
        url = "https://reaperscans.com/wp-admin/admin-ajax.php"
        items = reaper(url).getList(count,30)

        if len(items) == 0:
            break
        else:
            data.append(items)
        count = count + 1 
        if data == None:
            cache.clear()
    return response(data)

@reaperscans.route("/manga", methods=["GET"])
@cache.cached(timeout=50)
def getManga():
    url = request.args.get('url')
    if url == None:
        abort(make_error(400, "Bad Request", "url is required"))
    data = reaper(url).getManga()
    return response(data)


@reaperscans.route("/chapter", methods=["GET"])
@cache.cached(timeout=50)
def getChapter():
    url = request.args.get('url')
    if url == None:
        abort(make_error(400, "Bad Request", "url is required"))
    data = reaper(url).getChapter()
    return response(data)

