# coding: utf-8

import json


class UserEncoder(json.JSONEncoder):

    def default(self, obj):
        return obj.__dict__


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return self.__dict__


david = User('David', 'password')

ojson = david.to_json()
print(type(ojson))
print(ojson)
print(json.dumps(ojson))

