from flask import Flask, request, jsonify, make_response
import json
import vanitynumber
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
    is_valid_phone_number = vanitynumber.is_valid_phone_number(phone_number)

    response = {
        'success':True,
        'phone_number': phone_number,
        'is_valid': is_valid_phone_number
    }
    return make_response(jsonify(response), 200)



@app.route('/vanitynumbers', methods=['GET'])
def generate_vanitynumbers_from_phonenumber():
    if 'phone_number' not in request.args:
        response = {
            'success':False,
            'Error': 'Required argument (phone_number) Not provided'
        }
        return make_response(jsonify(response), 414) # Bad argument in request

    phone_number = request.args.get('phone_number')

    max_number_results = 100
    if 'max_number_results' in request.args:
        max_number_results = request.args.get('max_number_results')

    is_valid_phone_number = vanitynumber.is_valid_phone_number(phone_number)
    if not is_valid_phone_number:
        response = {
            'success':False,
            'phone_number': phone_number,
            'is_valid': is_valid_phone_number,
            'vanity_numbers': []
        }
        return make_response(jsonify(response), 400) # Bad Request

    possible_vanitynumbers = vanitynumber.all_wordifications(phone_number)
    # >>>vanitynumber.all_wordifications("1-800-266-5233")
    # >['1-800-BOOKBEE', '1-800-CNNJADE',...]

    response = {
        'success':True,
        'phone_number': phone_number,
        'vanitynumbers': possible_vanitynumbers
    }
    return make_response(jsonify(response), 200)

@app.route('/phonenumber', methods=['GET'])
def get_phonenumber_from_vanitynumber():
    if 'vanity_number' not in request.args:
        response = {
            'success':False,
            'Error': 'Required argument (vanity_number) Not provided'
        }
        return make_response(jsonify(response), 414) # Bad argument in request

    vanity_number = request.args.get('vanity_number')

    is_valid_vanitynumber = vanitynumber.is_valid_vanity_number(vanity_number)
    if not is_valid_vanitynumber:
        response = {
            'success':False,
            'vanity_number': vanity_number,
            'is_valid': is_valid_vanitynumber,
            'phonenumber': ""
        }
        return make_response(jsonify(response), 400) # Bad Request

    phone_number = vanitynumber.words_to_number(vanity_number)
    # >>>vanitynumber.words_to_number("1-866-COOLBEE")
    # >'1-866-266-5233'

    response = {
        'success':True,
        'vanity_number': vanity_number,
        'phone_number': phone_number
    }
    return make_response(jsonify(response), 200)
