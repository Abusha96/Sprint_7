import pytest
import requests

from tests.consts import Endpoints
from tests.helper import create_new_courier_and_return_payload


@pytest.fixture(scope="function")
def delete_courier():
    new_courier = create_new_courier_and_return_payload()
    response = requests.post(Endpoints.CREATE_COURIER, new_courier)
    yield

