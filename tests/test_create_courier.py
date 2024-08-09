import requests

from tests.consts import Endpoints
from tests.helper import create_new_courier_and_return_payload


class TestCreateCourier:
    def test_create_new_courier(self):
        expected_response = {'ok': True}
        new_courier = create_new_courier_and_return_payload()
        response = requests.post(Endpoints.CREATE_COURIER, new_courier)
        assert 201 == response.status_code and response.json() == expected_response

    def test_the_same_courier_cannot_be_created(self):
        expected_response = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        double_login = create_new_courier_and_return_payload()
        requests.post(Endpoints.CREATE_COURIER, double_login)
        response = requests.post(Endpoints.CREATE_COURIER, double_login)
        assert 409 == response.status_code and response.json() == expected_response

    def test_presence_of_required_fields(self):
        expected_response = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        data = create_new_courier_and_return_payload()
        for field in ['login', 'password']:
            value = data.pop(field)
            response = requests.post(Endpoints.CREATE_COURIER, data)
            assert 400 == response.status_code and response.json() == expected_response
            data[field] = value
