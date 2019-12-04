"""
utils functions
"""
import json


def load_config(config_file):
    """
    Load global configurations for json file
    """
    # Load configurations
    credentials = {}
    with open(config_file, "r") as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            credentials[k] = v
    return credentials
