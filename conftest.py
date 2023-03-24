import pytest
from modules.api.clients.rentberry import Rentberry


@pytest.fixture
def rentberry_api():
    api = Rentberry()
    yield api
