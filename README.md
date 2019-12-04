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

### Usage

Make a curl request to test de endpoint /tw-user-info/{twitter-user-name}

```
curl -v http://127.0.0.1:8000/twitter-consumer/user/milanesacosmika
```

## Running the tests

Running test with unittest

```
python -m unittest discover
```

## Deployment

Clone repository on your local machine or server and follow the install instructions.
```
git clone git@github.com:noctilukkas/twitter-consumer.git
```


## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Virtual environments for Python
* [Tweepy](https://www.tweepy.org/) - Twitter API wrapper for Python


## Author

* **Lucas Paiva** - [noctilukkas](https://github.com/noctilukkas)