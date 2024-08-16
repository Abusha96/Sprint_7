import pytest
import requests

from tests.consts import Endpoints
from tests.helper import create_courier_data


@pytest.fixture(scope="function")
def create_courier():
    new_courier = create_courier_data()
    response = requests.post(Endpoints.CREATE_COURIER, new_courier)
    yield new_courier, response
    response = requests.post(Endpoints.LOGIN, data=new_courier)
    requests.delete(Endpoints.CREATE_COURIER+f"/{response.json()['id']}")
