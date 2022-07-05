from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args] or error.description
    # print("message",message)
    # print("error",error.name)
    response = {
        'status': error.code,
        'error': {
            'type': error.name or error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response)