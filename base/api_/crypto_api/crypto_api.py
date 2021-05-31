import json
from json import JSONDecodeError

import requests

from base.api_.base_api import BaseApi
from base.constants import RESPONSE_TEXT
from config_definition import BaseConfig


class CryptoApi(BaseApi):
    def __init__(self):
        super(CryptoApi, self).__init__()

    def get_100_popular_currencies(self):
        uri = BaseConfig.AMBER_API_URL
        try:
            _response = requests.get(url=uri, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                print(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            print(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            print(F"{e.__class__.__name__} get_posts failed with error: {e}")
            raise e


if __name__ == "__main__":
    resp = CryptoApi().get_100_popular_currencies()
    print(resp)