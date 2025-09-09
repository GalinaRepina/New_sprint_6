import allure
import pytest
from helps.data import TestUsers
from pages.main_page import HomePage, HomePageHeader
from pages.order_page import OrderPage

class TestOrderPage: #по вашему замечанию я использую параметризация -  @pytest.mark.parametrize

    @allure.title('Тест оформления заказа самокатом')
    @allure.description('''Проверка оформления заказа через разные кнопки "Заказать"''')
    @pytest.mark.parametrize('user_data, order_button_type', [
        (TestUsers.FIRST_USER, 'header'),
        (TestUsers.SECOND_USER, 'home_page')
    ])
    def test_order_scooter(self, driver, user_data, order_button_type):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        
        home_page.accept_cookie_home_page()
        
        if order_button_type == 'header':
            header_page.order_button_click()
        else:
            home_page.scroll_and_click_on_the_order_button()
        
        order_page.order_scooter_full_path(user_data)
        assert order_page.check_order_title()