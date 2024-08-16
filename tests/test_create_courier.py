import allure
import requests

from tests.consts import Endpoints
from tests.helper import create_courier_data


class TestCreateCourier:
    @allure.title('Создание нового курьера')
    def test_create_new_courier(self, create_courier):
        expected_response = {'ok': True}
        payload, response = create_courier
        assert 201 == response.status_code and response.json() == expected_response

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_the_same_courier_cannot_be_created(self, create_courier):
        expected_response = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        payload, _ = create_courier
        response = requests.post(Endpoints.CREATE_COURIER, payload)
        assert 409 == response.status_code and response.json() == expected_response

    @allure.title('Проверка наличия обязательных полей')
    def test_presence_of_required_fields(self):
        expected_response = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        data = create_courier_data()
        for field in ['login', 'password']:
            value = data.pop(field)
            response = requests.post(Endpoints.CREATE_COURIER, data)
            assert 400 == response.status_code and response.json() == expected_response
            data[field] = value
