from flask import Flask, jsonify, request
from http import HTTPStatus
import re

app =  Flask(__name__)

payloads = [
    {
        'key': 'value'
    }
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route('/v1/sanitized/input/', methods=['GET'])
def get_payload():
    return jsonify({'data': payloads})

@app.route('/v1/sanitized/input/', methods=['POST'])
def create_payload():
    data = request.get_json()
    value = data.get('payload')

    #regex to find if the payload has sql injection characters or not
    regex = re.compile('[@_!$%^&*()<>?/\|}{~:]')

    if(regex.search(value) == None):
        sql_injection_flag = 1
    else:
        sql_injection_flag = 0

    if (sql_injection_flag == 1):

        value = 'sanitized'

        payload = {
        'result': value
        }

        return jsonify(payload), HTTPStatus.CREATED
    
    elif(sql_injection_flag == 0):

        value = 'unsanitized'

        payload = {
        'result': value
        }

        return jsonify(payload), HTTPStatus.FORBIDDEN
    
    else:
        return HTTPStatus.FORBIDDEN



