from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args] or error.description
    # print("message",message)
    response = {
        'status':  error.code if hasattr(error,'code') else 400,
        'error': {
            'type': error.name or error.__class__.__name__ or "",
            'message': message
        }
    }

    return jsonify(response)