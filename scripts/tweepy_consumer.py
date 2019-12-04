import tweepy
from tweepy.auth import OAuthHandler

# Authenticate to Twitter

credentials = {
  "consumer_api_key" : "GrvSyLQ25jg4VWn0jubWXvsqm",
  "consumer_api_secret_key" : "9TrMSO2qDXs0P9FrJ4q5xGPABUuVRV87CnWTpBlWbwLg9zoSif",
  "acces_token" : "139836920-hRoEK7wkgLQMLoLPzIqJNIObMmDbJS27fi4K4P95",
  "acces_token_secret" : "90KfAnqhpGII1VqC7RBMnk625kpsjcD8oBscmfEFw301X"
}

auth = OAuthHandler(credentials["consumer_api_key"], credentials["consumer_api_secret_key"])

auth.set_access_token(credentials["acces_token"], credentials["acces_token_secret"])

api = tweepy.API(auth)

# User target
info_user = api.get_user("c_spinetta")
user_followers_count = info_user.followers_count
# Followers
followers = api.followers("c_spinetta", count=user_followers_count)

for follower in followers:
    print("User name: {} - Follower count: {}".format(follower.screen_name, follower.followers_count))
