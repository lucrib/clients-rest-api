# coding=utf-8
import httplib as http

import jwt
from flask import jsonify, request
from flask_restful import Resource, marshal_with, fields

from client import api
from client import app
from client import db
from models import User


def valid_auth(auth):
    if auth.username == 'username' and auth.password == 'password':
        return True
    return False


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    if not auth:
        headers = {'WWW-Authenticate': "Basic realm='teste'"}
        return jsonify({'message': 'Authentication must be provided.'}), 401, headers

    if valid_auth(auth):
        payload = dict(username=auth.username, password=auth.password)
        jwt_data = jwt.encode(payload, app.config['SECRET_KEY'])
        return jsonify({"jwt": jwt_data}), 200

    return jsonify({'message': 'Invalid credentials.'}), 401


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'uri': fields.Url('user', absolute=True),
}


class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        data = request.get_json()
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user, http.CREATED


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user


api.add_resource(UserResource, '/users/<int:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')
