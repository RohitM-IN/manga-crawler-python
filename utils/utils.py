from flask import jsonify

def response(data,status=200,message="success"):

    return jsonify({'status': status , 'data' : data, 'message' : message})

def make_error(status_code, message, error):
    response = jsonify({
        'status': status_code,
        'error': {
            'message': message,
            'type': error
        }
    })
    response.status_code = status_code
    return response