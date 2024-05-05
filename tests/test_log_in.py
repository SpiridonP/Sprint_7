import requests
import allure


class TestCourierLogin:

    @allure.title('Вход в систему с валидными данными')
    @allure.step('Указать корректный логин и пароль')
    def test_login_in_system(self):
        payload = {
            "login": "narutohokage25",
            "password": "11234"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier/login", data=payload)
        assert response.status_code == 200
        data = response.json()
        assert data == {'id': 299643}

    @allure.title('Проверка входа с некорректным логином')
    @allure.step('В теле запроса указать некорректный логин')
    def test_incorrect_login_in(self):
        payload = {
            "login": "nrutohokage25",
            "password": "11234"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier/login", data=payload)
        assert response.status_code == 404
        data = response.json()
        assert data == {"message": "Учетная запись не найдена"}

    @allure.title('Проверка входа без логина')
    @allure.step('В теле запроса не указывать логин')
    def test_login_in_without_login(self):
        payload = {"password": "11234"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier/login", data=payload)
        assert response.status_code == 400
        data = response.json()
        assert data == {"message":  "Недостаточно данных для входа"}

    @allure.title('Проверка входа с данными несуществующего пользователя')
    @allure.step('В теле запроса указать данные несуществующего курьера')
    def test_login_in_nonexistent_courier(self):
        payload = {
            "login": "narutohokage)))",
            "password": "11234"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier/login", data=payload)
        assert response.status_code == 404
        data = response.json()
        assert data == {"message": "Учетная запись не найдена"}


