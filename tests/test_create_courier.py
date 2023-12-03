import pytest
import allure
import requests
import helpers
from data import Urls


class TestCreateCourier:

    @allure.title('Регистрация прошла успешно')
    def test_create_courier_success(self, not_registered_courier):
        payload = not_registered_courier
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Регистрация не прошла, курьер уже зарегистрирован в системе')
    def test_create_identical_couriers(self, not_registered_courier):
        payload = not_registered_courier
        requests.post(Urls.CREATE_COURIER, data=payload)
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Регистрация прошла успешно, заполнены только обязательные поля')
    def test_create_courier_without_name_not_successful(self, not_registered_courier):
        payload = not_registered_courier
        payload["firstName"] = None
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Регистрация не прошла , не заполнены обязательные поля')
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_create_courier_without_login_or_pass_not_successful(self, field):
        login, password, firstname = helpers.generate_login_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
        }
        del payload[field]
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
