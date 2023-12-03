import pytest
import requests
import allure
import helpers
from data import Urls


class TestLoginCourier:

    @allure.title('При успешной авторизации возвращается id')
    def test_login_courier_success(self, registered_courier):
        payload = registered_courier
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Авторизация не проходит , неверный логин или пароль')
    @pytest.mark.parametrize('field, incorrect_value', [("login", "incorrect"), ("password", "incorrect")])
    def test_login_courier_incorrect_log_or_pass(self, registered_courier, field, incorrect_value):
        payload = registered_courier.copy()
        payload[field] += incorrect_value
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title('Авторизация не проходит , не передан логин')
    def test_login_courier_empty_login_field(self):
        login, password, _ = helpers.generate_login_password()
        payload = {
            "password": password
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text

    @allure.title('Авторизация не проходит, не передан пароль')
    def test_login_courier_empty_pass_field(self):
        login, _, _ = helpers.generate_login_password()
        payload = {
            "login": login,
            "password": ""
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text

    @allure.title('Авторизация не проходит, пользователь не существует')
    def test_login_not_found_courier(self):
        login, password, firstname = helpers.generate_login_password()
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.text
