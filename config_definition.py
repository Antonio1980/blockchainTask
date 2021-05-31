import os
import configparser


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode="r", buffering=-1, closefd=True):
        parser.read(config)
        return parser


class BaseConfig:
    root_dir = os.path.abspath(os.path.dirname(__file__))

    config_file = os.path.join(root_dir, "config.cfg")
    parser = get_parser(config_file)

    AMBER_API_URL = parser.get("URL's", "amber_api_url")
    API_KEY = parser.get("ARG's", "api_key")

