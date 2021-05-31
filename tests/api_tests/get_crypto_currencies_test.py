import pytest
from base.constants import TEST_RESULT
from base.utils import Utils

test_case = "GET CRYPTO"


@pytest.mark.regression
class TestGetCrypto:

    def test_get_crypto_method_works(self, api_client):
        _response = api_client.get_100_popular_currencies()

        assert _response[0] is not None
        assert _response[1].status_code == 200
        assert _response[1].reason == "OK"

        print(TEST_RESULT.format(test_case, 1, "PASSED"))

    def test_print_all_crypto_prices(self, api_client):
        _response = api_client.get_100_popular_currencies()[0]

        assert isinstance(_response, dict)
        assert len(_response) > 0
        for obj in _response["data"]:
            assert isinstance(obj["quote"]["USD"]["price"], float)
            print(obj["quote"]["USD"]["price"])

        print(TEST_RESULT.format(test_case, 2, "PASSED"))

    def test_save_prices_into_file(self, api_client):
        _response = api_client.get_100_popular_currencies()[0]

        prices = list()
        for obj in _response["data"]:
            prices.append(obj["quote"]["USD"]["price"])

        srt = sorted(prices)
        file_ = "sorted_prices.csv"
        with open(file_, "r+") as f:
            f.truncate()
        for x in srt:
            Utils.save_into_file(x, file_)

        print(TEST_RESULT.format(test_case, 3, "PASSED"))

    def test_max_volume_in_market(self, api_client):
        _response = api_client.get_100_popular_currencies()[0]

        volumes = list()
        for obj in _response["data"]:
            volumes.append(obj["quote"]["USD"]["volume_24h"])

        vlm = sorted(volumes)[-1]

        for x in _response["data"]:
            assert vlm >= x["quote"]["USD"]["volume_24h"]

        print(vlm)

        print(TEST_RESULT.format(test_case, 4, "PASSED"))


