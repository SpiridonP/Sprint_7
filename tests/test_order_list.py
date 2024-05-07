import requests
import allure
import test_urls


class TestGetListOfOrders:

    @allure.title('Проверка получения заказов курьера')
    @allure.step('Отправить запрос указав id курьера')
    def test_get_order_list(self):
        response = requests.get(test_urls.check_order + "?courierId=299643")
        assert response.status_code == 200
        data = response.json()
        assert "orders" in data

