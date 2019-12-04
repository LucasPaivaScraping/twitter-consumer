import sys
sys.path.append('../')
import os
from flask import jsonify
from twitter.twitter import TwUser, TwFollower, TwitterClient
from utils.functions import load_config
from base.api import ApiRest
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE

obj_user = TwUser(10, "test_user", "test_username", "http://img.co", "", 200, "some")

tw_api = TwitterClient(load_config(TW_CREDENTIALS_FILE))

dirname = os.path.abspath(os.path.join(__file__, "../.."))
filename = os.path.join(dirname, 'credentials.json')
api_rest = ApiRest(filename, API_NAME, API_PORT)
print(type(api_rest))
print(api_rest)