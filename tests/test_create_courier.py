import allure
import requests

import payloads.create_courier_payloads
import test_urls
import data_answers
from payloads import create_courier_payloads

class TestCourierRegistration:

    @allure.title('Создание курьера')
    @allure.step('Заполнить поля в теле запроса для создания курьера')
    def test_creating_courier(self):
        payload = create_courier_payloads.correct_data

        response = requests.post(test_urls.create_courier, data=payload)
        assert response.status_code == 201
        data = response.json()
        assert data == {'ok': True}

    @allure.title('Создание курьера с существующим логином')
    @allure.step('В теле запроса указать существующий логин')
    def test_set_similar_login(self):
        payload = create_courier_payloads.correct_data

        response = requests.post(test_urls.create_courier, data=payload)
        assert response.status_code == 409
        data = response.json()
        assert data == data_answers.login_exist


    @allure.title('При создании курьера не указать обязательное поле')
    @allure.step('В теле запроса не указать пароль')
    def test_creating_courier_without_required_fields(self):
        payload = payloads.create_courier_payloads.no_password

        response = requests.post(test_urls.create_courier, data=payload)
        assert response.status_code == 400
        data = response.json()
        assert data == data_answers.not_enough_data



