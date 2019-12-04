# twitter-consumer

A simple api-consumer / crawler for Twitter . Developed for Python 3 and Flask 1.1.1

### Installing

create a virtual environment with virtualenv with python 3

```
python -m venv venv
```
or hidden directory
```
python -m venv .env
```

Next activate virtual environment
```
source /venv/bin/activate
```


Install all dependences with PIP

```
pip install -r requirements.txt
```

### Setup application

Edit credentials.json file with valid credentials for twitter developer account
```
{
  "consumer_api_key" : "",
  "consumer_api_secret_key" : "",
  "acces_token" : "",
  "acces_token_secret" : ""
}
```

You can setup custom settings in utils.config :
```
API_NAME = "twitter-consumer"
API_PORT = 8000
TW_CREDENTIALS_FILE = "credentials.json"
```

## Running the APP
For starting virtual environment and API, just
```
sh ./run.sh
```

### Usage

Make a curl request to test the endpoint /tw-user-info/{twitter-user-name}
You can setup custom values for Api Port
```
curl -v http://127.0.0.1:8000/twitter-consumer/user/milanesacosmika
```

## Running the tests

Running test with unittest

```
python -m unittest tests.test_basic
```

## Deployment

Clone repository on your local machine or server and follow the install instructions.
```
git clone git@github.com:noctilukkas/twitter-consumer.git
```
*Note:
This app was developed and tested on Mac OS (Darwin)

## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Virtual environments for Python
* [Tweepy](https://www.tweepy.org/) - Twitter API wrapper for Python


## Author

* **Lucas Paiva** - [noctilukkas](https://github.com/noctilukkas)