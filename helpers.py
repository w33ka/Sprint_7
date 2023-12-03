import requests
from faker import Faker

fake = Faker()


def generate_login_password():
    login = fake.user_name()
    password = fake.password()
    firstname = fake.first_name()
    return login, password, firstname


def register_courier_return_login_password():
    login, password, firstname = generate_login_password()

    payload = {
        "login": login,
        "password": password,
        "firstName": firstname
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    return (login, password, firstname) if response.status_code == 201 else None

