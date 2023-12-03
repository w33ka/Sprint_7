import requests
import allure
from data import Urls


class TestOrderList:

    @allure.title('Возврат списка заказов в тело ответа')
    def test_order_list(self):
        response = requests.get(Urls.ORDER_LIST)
        list_orders = response.json()['orders']
        assert response.status_code == 200 and len(list_orders) != 0
