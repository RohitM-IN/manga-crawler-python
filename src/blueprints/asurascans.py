from flask import Blueprint, jsonify, request, abort
from utils.cleaner import asura, response, make_error
from werkzeug.exceptions import BadRequest



asurascans = Blueprint(name="asurascans", import_name=__name__)


@asurascans.route("/asura", methods=["GET"])
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

    return response(data)

@asurascans.route("/asura/manga", methods=["GET"])
def getManga():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    data = asura(url).getManga()

    return response(data)


@asurascans.route("/asura/chapter", methods=["GET"])
def getChapter():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    data = asura(url).getChapter()

    return response(data)

