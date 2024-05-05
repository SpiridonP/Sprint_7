import allure
import pytest
import requests

test_data = [
    ({"firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": "Преображенская площадь", "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06", "comment": "Saske, come back to Konoha", "color": ["BLACK"]}, 201),
    ({"firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": "Преображенская площадь", "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06", "comment": "Saske, come back to Konoha", "color": ["BLACK", "GREY"]}, 201),
    ({"firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": "Преображенская площадь", "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06", "comment": "Saske, come back to Konoha"}, 201)
]

class TestOrder:
    @allure.title('Проверка создания заказа')
    @allure.step('В теле запроса указать 1 цвет, 2 цвета, не указывать цвет')
    @pytest.mark.parametrize("payload, expected_status_code", test_data)
    def test_create_order(self, payload, expected_status_code):
        response = requests.post("https://qa-scooter.praktikum-services.ru/" + "api/v1/orders", json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        assert 'track' in data
        print(data)


