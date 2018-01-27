from faker import Faker
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

VERSION = '0.1.0'

app = Flask('User')

app.config['SECRET_KEY'] = 'LUCAS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thisisatest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
faker = Faker()
