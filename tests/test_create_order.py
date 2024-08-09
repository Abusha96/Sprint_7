import json

import pytest
import requests

from tests.consts import Endpoints


class TestCreateOrder:
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
        print(data)
        response = requests.post(Endpoints.CREATE_ORDER, json_data)
        assert 201 == response.status_code and 'track' in response.json()


    def test_get_list_of_orders(self):
        pass
