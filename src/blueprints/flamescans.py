from flask import Blueprint, request
from utils.cleaners.flame import flame
from utils.cache import cache, getCache
from utils.utils import response, make_error
from config import CACHE_TIME
import numpy as np

flamescans = Blueprint(name="flame", import_name=__name__)

@flamescans.route("/", methods=["GET"])
@cache.cached(timeout=CACHE_TIME)
def getList():
    data = []
    count = 0
    while True:
        url = "https://flamescans.org/series/?order=update&page=" + str(count)
        items = flame(url).getList()
    
        if len(items) == 0:
            break
        else:
            data.append(items)
        count = count + 1 
        if data == None:
            cache.clear()
    items = list(np.concatenate(data).flat)
    return response(items)


@flamescans.route("/manga", methods=["GET"])
def getManga():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")

    def callback():
        return flame(url).getManga()
    data = getCache(url,callback)

    if data == False:
        return make_error(400, "Flame Scans returned 404 for the given url", "Invalid Url")

    return response(data)


@flamescans.route("/chapter", methods=["GET"])
def getChapter():
    url = request.args.get("url")
    if url == None:
        return make_error(400, "Invalid or missing url parameter", "Missing Parameter")
    def callback():
        return flame(url).getChapter()
    data = getCache(url,callback)
    if data == False:
        return make_error(400, "Flame Scans returned 404 for the given url", "Invalid Url")
    return response(list(filter(None,data)))