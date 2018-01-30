# coding=utf-8

import jwt
from flask import request
from flask_restful import Resource
from client import app


def valid_auth(auth):
    if auth.username == 'username' and auth.password == 'password':
        return True
    return False


class LoginResource(Resource):

    def get(self):
        auth = request.authorization
        if not auth:
            headers = {'WWW-Authenticate': "Basic realm='teste'"}
            return {'message': 'Authentication must be provided.'}, 401, headers

        if valid_auth(auth):
            payload = dict(username=auth.username, password=auth.password)
            jwt_data = jwt.encode(payload, app.config['SECRET_KEY'])
            return {"jwt": jwt_data}, 200

        return {'message': 'Invalid credentials.'}, 401



