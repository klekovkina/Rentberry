import pytest
import requests
import time
from modules.api.clients.rentberry import Rentberry


# Test checks that response of POST request consist the url with
# correct searching request result
@pytest.mark.api
def test_search_location_positive(rentberry_api):
    resp_locat = rentberry_api.search_location("Kyiv, Ukraine")
    assert (
        resp_locat["body"]["url"]
        == "https://rentberry.com/ua/apartments/s/kyiv-ukraine-02000"
    )


# Test checks the download time of main page is less then 0,4s
@pytest.mark.api
def test_download_time():
    start_time = time.time()
    r = requests.get("https://rentberry.com/")
    end_time = time.time()
    download_time = end_time - start_time
    assert r.status_code == 200
    assert download_time < 0.4


# Test the login
@pytest.mark.api
def test_login(rentberry_api):
    # Replace the values for username and password with actual credentials
    r = rentberry_api.login("username", "password")
    assert r is not None
