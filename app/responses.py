from flask import jsonify

# Respuesta exitosa
def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200