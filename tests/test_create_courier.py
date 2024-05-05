import allure
import requests



class TestCourierRegistration:

    @allure.title('Создание курьера')
    @allure.step('Заполнить поля в теле запроса для создания курьера')
    def test_creating_courier(self):
        payload = {
            "login": "narutohokage28",
            "password": "11234",
            "firstNam": "madara"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier", data=payload)
        assert response.status_code == 201
        data = response.json()
        assert data == {'ok': True}

    @allure.title('Создание курьера с существующим логином')
    @allure.step('В теле запроса указать существующий логин')
    def test_set_similar_login(self):
        payload = {
            "login": "narutohokage28",
            "password": "11234",
            "firstNam": "madara"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier", data=payload)
        assert response.status_code == 409
        data = response.json()
        assert data == {'message': 'Этот логин уже используется'}


    @allure.title('При создании курьера не указать обязательное поле')
    @allure.step('В теле запроса не указать пароль')
    def test_creating_courier_without_required_fields(self):
        payload = {
            "login": "narutohokage18",
            "firstNam": "madara"}

        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/courier", data=payload)
        assert response.status_code == 400
        data = response.json()
        assert data == {'message': 'Недостаточно данных для создания учетной записи'}



