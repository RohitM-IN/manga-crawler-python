from flask import Blueprint, jsonify, request, abort
from utils.cleaner import asura
from werkzeug.exceptions import BadRequest
from utils.cache import cache
from utils.utils import response, make_error

asurascans = Blueprint(name="asurascans", import_name=__name__)

@asurascans.route("/", methods=["GET"])
@cache.cached(timeout=50)
def getList():
    data = []
    count = 1
    while True:
        url = "https://www.asurascans.com/manga/?status=&type=&order=title&page=" + str(count)
        items = asura(url).getList()

        if len(items) == 0:
            break
        else:
            data.append(items)
        count = count + 1 
        if data == None:
            cache.clear()
    return response(data)

@asurascans.route("//manga", methods=["GET"])
@cache.cached(timeout=50)
def getManga():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    data = asura(url).getManga()

    if data == None:
        cache.clear()

    return response(data)


@asurascans.route("//chapter", methods=["GET"])
@cache.cached(timeout=50)
def getChapter():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    data = asura(url).getChapter()
    if data == None:
        cache.clear()
    return response(list(filter(None,data)))