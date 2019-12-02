from flask import jsonify

# Respuesta 400
def bad_request():
    return jsonify({
        'success': False,
        'data':{},
        'message':'Bad request',
        'code':400
    }), 400

# Respuesta 200
def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200

# Respuesta 404
def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found'
        }
    ), 404