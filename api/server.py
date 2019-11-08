from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

# Ping
@app.route('/')
def index():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/validate', methods=['GET'])
def validate():
    if 'phone_number' not in request.args:
        response = {
            'success':False,
            'Error': 'Required argument (phone_number) Not provided'
        }
        return make_response(jsonify(response), 414)

    phone_number = request.args.get('phone_number')
    response = {
        'success':True,
        'phone_number': phone_number,
        'is_valid': True
    }
    return make_response(jsonify(response), 200)
