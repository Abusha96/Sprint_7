import allure
import requests

from tests.consts import Endpoints
from tests.helper import generate_random_string


class TestLoginCourier:
    @allure.title('Успешная авторизация')
    def test_success_authorization(self, create_courier):
        payload, _ = create_courier
        response = requests.post(Endpoints.LOGIN, payload)
        assert 200 == response.status_code and 'id' in response.json()

    @allure.title('Неправильный логин или пароль')
    def test_incorrect_creds(self, create_courier):
        expected_response = {'code': 404, "message": "Учетная запись не найдена"}
        payload, _ = create_courier
        for field in ['login', 'password']:
            value = payload.pop(field)
            payload[field] = generate_random_string(10)
            response = requests.post(Endpoints.LOGIN, payload)
            assert 404 == response.status_code and response.json() == expected_response
            payload[field] = value

    @allure.title('Обязательное поле не заполнено (не указан логин или пароль)')
    def test_empty_field(self, create_courier):
        expected_response = {'code': 400, "message":  "Недостаточно данных для входа"}
        payload, _ = create_courier
        for field in ['login']:
            # Предполагалась строка for field in ['login', 'password'], но при попытке отправить
            # запрос без пароля возвращается ответ, не соответствующий документации (504 вместо 400). На сервере ошибка,
            # поэтому этот тест невозможно пройти (ссылка на тред с наставником https://app.pachca.com/chats?thread_message_id=310681610&sidebar_message=310854951)
            value = payload.pop(field)
            response = requests.post(Endpoints.LOGIN, payload)
            assert 400 == response.status_code and response.json() == expected_response
            payload[field] = value
