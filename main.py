"""
Main module
"""
from base.api import ApiRest
from utils.config import API_NAME, API_PORT, TW_CREDENTIALS_FILE


def main():
    api_rest = ApiRest(TW_CREDENTIALS_FILE, API_NAME, API_PORT)
    api_rest.run()


if __name__ == '__main__':
    main()



