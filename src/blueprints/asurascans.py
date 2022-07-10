from flask import Blueprint, request
from utils.cleaners.asura import asura
from utils.cache import cache, getCache
from utils.utils import response, make_error
from config import CACHE_TIME
import numpy as np

asurascans = Blueprint(name="asurascans", import_name=__name__)

@asurascans.route("/", methods=["GET"])
@cache.cached(timeout=CACHE_TIME)
def getList():
    data = []
    count = 1
    while True:
        url = "https://www.asurascans.com/manga/?status=&type=&order=update&page=" + str(count)
        items = asura(url).getList()
        if len(items) == 0:
            break
        else:
            data.append(items)
        count = count + 1 
        if data == None:
            cache.clear()
    items = list(np.concatenate(data).flat)

    return response(items)

@asurascans.route("/manga", methods=["GET"])
def getManga():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")

    def callback():
        return asura(url).getManga()
    data = getCache(url,callback)

    if data == False:
        return make_error(400, "Asura Scans returned 404 for the given url", "Invalid Url")

    return response(data)


@asurascans.route("/chapter", methods=["GET"])
def getChapter():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    def callback():
        return asura(url).getChapter()

    data = getCache(url,callback)

    if data == False:
        return make_error(400, "Asura Scans returned 404 for the given url", "Invalid Url")
        
    return response(list(filter(None,data)))