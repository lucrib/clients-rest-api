import json


class Serializable(object):
    def __init__(self):
        pass

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Client(Serializable):
    def __init__(self, name, date_of_birth, email, id_=None):
        super(Client, self).__init__()
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.id_ = id_
