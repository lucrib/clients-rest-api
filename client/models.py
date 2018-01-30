from client import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    age = db.Column('age', db.Integer)
    birthdate = db.Column('birthdate', db.String)
    email = db.Column('email', db.String)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String)

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
