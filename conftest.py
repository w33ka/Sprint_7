import pytest
import requests
import helpers
from data import Urls


@pytest.fixture
def not_registered_courier():
    login, password, firstname = helpers.generate_login_password()
    payload = {
        "login": login,
        "password": password,
        "firstName": firstname
    }

    yield payload
    del payload["firstName"]
    response = requests.post(Urls.LOGIN_COURIER, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{Urls.CREATE_COURIER}{courier_id}')


@pytest.fixture
def registered_courier():
    login, password, firstname = helpers.register_courier_return_login_password()
    payload = {
        "login": login,
        "password": password
    }

    yield payload
    response = requests.post(Urls.LOGIN_COURIER, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{Urls.CREATE_COURIER}{courier_id}')