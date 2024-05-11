import requests
import allure
import test_urls
import data_answers
from payloads import create_log_in_payloads

class TestCourierLogin:

    @allure.title('Вход в систему с валидными данными')
    @allure.step('Указать корректный логин и пароль')
    def test_login_in_system(self):
        payload = create_log_in_payloads.correct_data

        response = requests.post(test_urls.log_in, data=payload)
        assert response.status_code == 200
        data = response.json()
        assert data == {'id': 299643}

    @allure.title('Проверка входа с некорректным логином')
    @allure.step('В теле запроса указать некорректный логин')
    def test_incorrect_login_in(self):
        payload = create_log_in_payloads.incorrect_login

        response = requests.post(test_urls.log_in, data=payload)
        assert response.status_code == 404
        data = response.json()
        assert data == data_answers.account_not_found

    @allure.title('Проверка входа без логина')
    @allure.step('В теле запроса не указывать логин')
    def test_login_in_without_login(self):
        payload = create_log_in_payloads.without_login

        response = requests.post(test_urls.log_in, data=payload)
        assert response.status_code == 400
        data = response.json()
        assert data == data_answers.not_enough_data_for_log_in

    @allure.title('Проверка входа с данными несуществующего пользователя')
    @allure.step('В теле запроса указать данные несуществующего курьера')
    def test_login_in_nonexistent_courier(self):
        payload = create_log_in_payloads.non_existent_courier

        response = requests.post(test_urls.log_in, data=payload)
        assert response.status_code == 404
        data = response.json()
        assert data == data_answers.account_not_found


