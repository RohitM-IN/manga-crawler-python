from flask import Blueprint, jsonify, request, abort
from utils.cleaner import reaper
from werkzeug.exceptions import BadRequest
from utils.cache import cache, getCache
from utils.utils import response, make_error
import os

reaperscans = Blueprint(name="Reaper", import_name=__name__)

@reaperscans.route("/", methods=["GET"])
@cache.cached(timeout=int(os.getenv('CACHE_TIME')))
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
def getManga():
    url = request.args.get('url')
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    def callback():
        return reaper(url).getManga()
    
    data = getCache(url,callback)

    return response(data)


@reaperscans.route("/chapter", methods=["GET"])
@cache.cached(timeout=int(os.getenv('CACHE_TIME')))
def getChapter():
    url = request.args.get('url')
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    def callback():
        return reaper(url).getChapter()
    data = getCache(url,callback)
    return response(data)

