# coding=utf-8
import httplib as http

import jwt
from faker import Faker
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LUCAS'
api = Api(app)
faker = Faker()

CLIENTS = [
    {'id': 1, 'name': 'Lucas Ribeiro', 'date_of_birth': '16/01/1990', 'email': 'lucas@ribeiro.com'},
    {'id': 2, 'name': 'Maria Angélica Nieli', 'date_of_birth': '11/04/1994', 'email': 'maria@ribeiro.com'},
    {'id': 3, 'name': 'Gustavo Ribeiro', 'date_of_birth': '22/10/1991', 'email': 'gusatvo@ribeiro.com'},
]


def valid_auth(auth):
    if auth.username == 'username' and auth.password == 'password':
        return True
    return False


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    print('aaaaaaaaa', auth)
    if not auth:
        return jsonify({'message': 'Invalid credentials.'}), 999

    if valid_auth(auth):
        payload = dict(username=auth.username, password=auth.password)
        jwt_data = jwt.encode(payload, app.config['SECRET_KEY'])
        return jsonify({"jwt": jwt_data}), 200

    return jsonify({'message': 'Invalid credentials.'}), 401


class ClientAPI(Resource):
    def get(self):
        return jsonify({'clients': CLIENTS})

    def post(self):
        # data = dir(request.form)
        data = request.form
        return data, http.CREATED


api.add_resource(ClientAPI, '/clients', endpoint='clients')

if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True, port='5000')
