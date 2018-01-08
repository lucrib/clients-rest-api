from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from client import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    birthdate = Column('birthdate', String)
    email = Column('email', String)
    username = Column('username', String)
    password = Column('password', String)

    def __init__(self, id=None, name=None, age=None, username=None, password=None, email=None, birthdate=None):
        self.id = id
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return u'User(id={})'.format(self.id)

    def __str__(self):
        return u'User(id={}, username={}, name={}, email{})'.format(self.id, self.username, self.name, self.email)


db.create_all()
