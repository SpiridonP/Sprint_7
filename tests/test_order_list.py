import requests
import allure



class TestGetListOfOrders:

    @allure.title('Проверка получения заказов курьера')
    @allure.step('Отправить запрос указав id курьера')
    def test_get_order_list(self):
        response = requests.get("https://qa-scooter.praktikum-services.ru/" + "api/v1/orders?courierId=299643")
        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        print(data)

