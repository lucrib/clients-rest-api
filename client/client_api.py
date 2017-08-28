# coding=utf-8
import httplib as http

from faker import Faker
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
faker = Faker()

CLIENTS = [
    {'id': 1, 'name': 'Lucas Ribeiro', 'date_of_birth': '16/01/1990', 'email': 'lucas@ribeiro.com'},
    {'id': 2, 'name': 'Maria Angélica Nieli', 'date_of_birth': '11/04/1994', 'email': 'maria@ribeiro.com'},
    {'id': 3, 'name': 'Gustavo Ribeiro', 'date_of_birth': '22/10/1991', 'email': 'gusatvo@ribeiro.com'},
]


class ClientAPI(Resource):
    def get(self):
        return jsonify({'clients': CLIENTS})

    def post(self):
        # data = dir(request.form)
        data = request.form
        return data, http.CREATED


api.add_resource(ClientAPI, '/clients', endpoint='clients')

if __name__ == '__main__':
    app.run(debug=True)
