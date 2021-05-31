from config_definition import BaseConfig


class BaseApi:
    def __init__(self):
        self.api_url = BaseConfig.AMBER_API_URL
        self.headers = {'Content-Type': "application/json", 'charset': 'UTF-8', "X-CMC_PRO_API_KEY": BaseConfig.API_KEY,
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
