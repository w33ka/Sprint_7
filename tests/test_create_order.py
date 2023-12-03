import pytest
import requests
import allure
from data import Urls


class TestCreateOrder:
    @allure.title('Заказ самоката с различными цветами прошел успешно')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Vika",
            "lastName": "Ananeva",
            "address": "Moskovskaya, 45",
            "metroStation": 4,
            "phone": "+7 999 852 45 78",
            "rentTime": 5,
            "deliveryDate": "2023-12-24",
            "comment": "Zhdu samokat, skoree!",
            "color": color
        }
        response = requests.post(Urls.CREATE_ORDER, params=payload)
        assert response.status_code == 201 and "track" in response.json()
