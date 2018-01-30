from login import LoginResource
from user import UserResource, UserListResource
from client import api

api.add_resource(LoginResource, '/login', endpoint='login')
api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')
