from flask import Blueprint, request
from utils.cleaners.realm import realm
from utils.cache import cache, getCache
from utils.utils import response, make_error
from config import CACHE_TIME
import numpy as np

realmscans = Blueprint(name="realmscans", import_name=__name__)

@realmscans.route("/", methods=["GET"])
@cache.cached(timeout=CACHE_TIME)
def getList():
    data = []
    count = 1
    while True:
        url = "https://realmscans.com/series/?status=&type=&order=update&page=" + str(count)
        items = realm(url).getList()
        if len(items) == 0:
            break
        else:
            data.append(items)
        count = count + 1 
        if data == None:
            cache.clear()
    items = list(np.concatenate(data).flat)

    return response(items)

@realmscans.route("/manga",methods=["GET"])
def getManga():
    data = None
    url = request.args.get('url')
    if url == None:
        return make_error("No url provided")

    def callback():
        return realm(url).getManga()
    data = getCache(url,callback)
    
    if data == False:
        return make_error(400, "Realm Scans returned 404 for the given url", "Invalid Url")
    return response(data)

@realmscans.route("/chapter",methods=["GET"])
def getChapter():
    data = None
    url = request.args.get('url')
    if url == None:
        return make_error("No url provided")

    def callback():
        return realm(url).getChapter()
    data = getCache(url,callback)

    if data == False:
        return make_error(400, "Realm Scans returned 404 for the given url", "Invalid Url")
    return response(data)