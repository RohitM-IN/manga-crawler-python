from flask import Blueprint, jsonify, request
from utils.cleaner import asura, response



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
    data = asura(url).getManga()
    # html = crawler(url)


    return response(data)



# def index():
#     return scraper.get("http://asurascans.com").content