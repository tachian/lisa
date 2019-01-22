import pytest

from lisa.app import api
from falcon import testing

@pytest.fixture()
def client():
    return testing.TestClient(api)