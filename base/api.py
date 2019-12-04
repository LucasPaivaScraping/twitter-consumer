from flask import Flask
from flask_restful import Api, Resource
from flask import jsonify

from twitter.twitter import TwUser, TwFollower, TwitterClient
from utils.functions import load_config
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE

app = Flask(__name__)


class ApiRest(object):
    def __init__(self, credentials, api_name, api_port):
        self.api = Api(app)
        self.app = app #Bad idea
        self.credentials = credentials
        self.api_name = api_name
        self.api_port = api_port

    def run(self):
        app.run(port=self.api_port)

    @staticmethod
    @app.route('/health-check')
    def index():
        return 'ok!'
