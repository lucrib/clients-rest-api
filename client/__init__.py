from flask_restful import Api
from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

VERSION = '0.1.0'

app = Flask('User')
api = Api(app)
db = SQLAlchemy(app)
faker = Faker()

app.config['SECRET_KEY'] = 'LUCAS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thisisatest.db'

import apis
