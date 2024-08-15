import json

import allure
import pytest
import requests

from tests.consts import Endpoints


class TestCreateOrder:
    @allure.title('Создание заказа и возврат его трек номера')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        json_data = json.dumps(data)
        response = requests.post(Endpoints.ORDERS, json_data)
        assert 201 == response.status_code and 'track' in response.json()
        requests.put(Endpoints.CANCEL_ORDER, response.json())

    @allure.title('Получение списка всех заказов')
    def test_get_list_of_orders(self):
        response = requests.get(Endpoints.ORDERS)
        assert 200 == response.status_code and 'orders' in response.json()
