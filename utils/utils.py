from flask import jsonify, Response
import re
from urllib.parse import urlparse, urlunparse

def response(data,status=200,message="success"):

    return jsonify({'status': status , 'data' : data, 'message' : message}), status

def make_error(status_code, message, error):
    response = jsonify({
        'status': status_code,
        'error': {
            'message': message,
            'type': error
        }
    })
    response.code = status_code
    return response, status_code

def chapterFixer(str):
    output = ""
    if re.match('Chapter', str,re.I):
        output = str.capitalize()
    else:
        output = 'Chapter ' + str
    return output

def checkCloudflare(parsed_html):

    if parsed_html.find('span',{'class':'cf-error-code'}):
        return parsed_html.find('span',{'class':'cf-error-code'}).get_text(strip=True)
    else:
        return 200

def checkError(data):
    if data == False:
        return make_error(400, "Website returned 404 for the given url", "Url Error")
    # elif data.isnumeric():
    #     return make_error( 400, "Cloudflare has returned " + data + " for the given url", "Cloudflare Error")
    return False

def fixUrl(url):
    return urlunparse(urlparse(url,"https")) 