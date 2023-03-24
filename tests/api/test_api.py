import pytest
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
    # print(resp_locat)
