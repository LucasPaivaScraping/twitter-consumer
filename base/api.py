from flask import Flask
from flask_restful import Api, Resource
from flask import jsonify

from twitter.twitter import TwUser, TwFollower, TwitterClient
from utils.functions import load_config
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE

app = Flask(__name__)
api = Api(app)


class ApiRest(object):
    def __init__(self, credentials, api_name, api_port):
        #self.api = Api(app)
        #self.app = app #Bad idea
        self.credentials = credentials
        self.api_name = api_name
        self.api_port = api_port

    def run(self):
        app.run(port=self.api_port)

    @api.app.route('/{}/tw-user-info/<user_name>'.format(API_NAME), methods=['get'])
    def get_user_info(user_name):
        try:
            # First check valid credentials
            tw_api = TwitterClient(load_config(TW_CREDENTIALS_FILE))
            tw_api.check_credentials()
            # Get profile data from user target
            info_user = tw_api.get_user_data(user_name)
            tw_user = TwUser(
                info_user.id,
                info_user.screen_name,
                info_user.name,
                info_user.profile_image_url,
                info_user.profile_location,
                info_user.followers_count,
                info_user.description
            )
            # Get followers data from user target
            followers_items = tw_api.get_followers(user_name, tw_user.followers_count)
            followers = []
            for item in followers_items:
                tw_follower = TwFollower(item.id,
                                         item.screen_name,
                                         item.name,
                                         item.followers_count)

                followers.append(tw_follower.to_json())

            return jsonify({
                "user": tw_user.to_json(),
                "followers": followers
            }), 200

        except Exception as e:
            return jsonify({
                "error": "Cant retrieve data from twitter"
            }), 403

    @staticmethod
    @app.route('/health-check')
    def index():
        return 'ok!'
