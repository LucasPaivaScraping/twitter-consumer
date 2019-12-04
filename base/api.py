from flask import Flask
from flask_restful import Api


class ApiRest(object):
    def __init__(self, credentials, api_name, api_port):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.credentials = credentials
        self.api_name = api_name
        self.api_port = api_port

    def run(self):
        self.app.run(port=self.api_port)
