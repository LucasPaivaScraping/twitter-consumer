"""
Main module
"""
from flask import jsonify
from twitter.twitter import TwUser, TwFollower, TwitterClient
from utils.functions import load_config
from base.api import ApiRest
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE


def main():

    api_rest = ApiRest(TW_CREDENTIALS_FILE, API_NAME, API_PORT)
    tw_api = TwitterClient(load_config(TW_CREDENTIALS_FILE))

    @api_rest.app.route('/{}/user/<user_name>'.format(API_NAME), methods=['get'])
    def get_user_info(user_name):
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
        followers_items = tw_api.get_followers(user_name)
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
        })

    api_rest.run()


if __name__ == '__main__':
    main()



