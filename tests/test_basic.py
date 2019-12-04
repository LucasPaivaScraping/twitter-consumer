import sys
sys.path.append('../')
import os

import unittest
from flask import Flask

from twitter.twitter import TwUser, TwFollower, TwitterClient
from utils.functions import load_config
from base.api import ApiRest
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE


class BasicTests(unittest.TestCase):

    def test_user_target_isinsctance_of_twuser(self):
        obj_user = TwUser(10, "test_user", "test_username", "http://img.co", "", 200, "some")
        self.assertIsInstance(obj_user, TwUser)

    def test_follower_is_isinstance_of_twfollower(self):
        obj_follower = TwFollower(10, "test_user", "test_screen_name", 100)
        self.assertIsInstance(obj_follower, TwFollower)

    def test_twapi_is_instance_of_twclient(self):
        dirname = os.path.abspath(os.path.join(__file__, "../.."))
        filename = os.path.join(dirname, TW_CREDENTIALS_FILE)
        obj_tw_api = TwitterClient(load_config(filename))
        self.assertIsInstance(obj_tw_api, TwitterClient)

    def test_apirest_isinstance_of_apirest(self):
        obj_api_rest = ApiRest(TW_CREDENTIALS_FILE, API_NAME, API_PORT)
        self.assertIsInstance(obj_api_rest, ApiRest)

    def test_taget_user_is_expected(self):
        dirname = os.path.abspath(os.path.join(__file__, "../.."))
        filename = os.path.join(dirname, TW_CREDENTIALS_FILE)
        obj_tw_api = TwitterClient(load_config(filename))
        obj_info_user = obj_tw_api.get_user_data("milanesacosmika")
        self.assertEqual(obj_info_user.id, 139836920)

    def test_target_user_has_followers(self):
        dirname = os.path.abspath(os.path.join(__file__, "../.."))
        filename = os.path.join(dirname, TW_CREDENTIALS_FILE)
        obj_tw_api = TwitterClient(load_config(filename))
        obj_followers_user = obj_tw_api.get_followers("milanesacosmika")
        self.assertNotEqual(len(obj_followers_user), 0)

    def test_apirest_get_user(self):
        app = Flask(__name__)

        with app.app_context():
            obj_api_rest = ApiRest(TW_CREDENTIALS_FILE, API_NAME, API_PORT)
            res = obj_api_rest.get_user_info("milanesacosmika")
        self.assertEqual(res[0].status_code, 200)


if __name__ == "__main__":
    unittest.main()
