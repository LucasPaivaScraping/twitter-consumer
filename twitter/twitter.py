import tweepy
from tweepy.auth import OAuthHandler


class TwitterClient(object):
    """
    Tweepy wrapper
    """
    user_profile_data = None
    followers = None

    def __init__(self, config):
        self.auth = OAuthHandler(config["consumer_api_key"],
                                 config["consumer_api_secret_key"])
        self.auth.set_access_token(config["acces_token"],
                                   config["acces_token_secret"])
        self.api_twitter = tweepy.API(self.auth)

    def get_user_data(self, user_name):
        self.user_profile_data = self.api_twitter.get_user(user_name)
        return self.user_profile_data

    def get_followers(self, user_name):
        self.followers = self.api_twitter.followers(user_name, count=self.user_profile_data.followers_count)
        return self.followers

    def credential_validation(self):
        pass

    def get_instance(self):
        pass


class TwUser(object):
    """
    Twitter users class
    id
    screen_name
    name
    profile_image_url
    profile_location
    followers_count
    description
    """

    def __init__(self, user_id, screen_name, name, profile_image_url, profile_location, followers_count, description):
        self.id = user_id
        self.screen_name = screen_name
        self.name = name
        self.profile_image_ur = profile_image_url
        self.profile_location = profile_location
        self.followers_count = followers_count
        self.description = description

    def to_json(self):
        return self.__dict__


class TwFollower(object):
    """
    Twitter follower class
    id
    follower_id
    screen_name
    followers_count
    """

    def __init__(self, follower_id, screen_name, name, followers_count):
        self.follower_id = follower_id
        self.screen_name = screen_name
        self.name = name
        self.followers_count = followers_count

    def to_json(self):
        return self.__dict__
