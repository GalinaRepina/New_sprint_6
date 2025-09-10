import allure
import pytest
from helps.data import TestUsers
from pages.main_page import HomePage, HomePageHeader
from pages.order_page import OrderPage
from config.urls import app_config

class TestOrderPage:

    @allure.title('Тест оформления заказа самокатом через кнопку в хедере')
    @allure.description('''Проверка оформления заказа через кнопку "Заказать" в хедере''')
    @pytest.mark.parametrize('user_data', [TestUsers.FIRST_USER])
    def test_order_scooter_via_header_button(self, driver, user_data):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        
        home_page.accept_cookie_home_page()
        header_page.order_button_click()
        
        order_page.order_scooter_full_path(user_data)
        assert order_page.check_order_title()

    @allure.title('Тест оформления заказа самокатом через кнопку на главной странице')
    @allure.description('''Проверка оформления заказа через кнопку "Заказать" на главной странице''')
    @pytest.mark.parametrize('user_data', [TestUsers.SECOND_USER])
    def test_order_scooter_via_home_page_button(self, driver, user_data):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        
        home_page.accept_cookie_home_page()
        home_page.scroll_and_click_on_the_order_button()
        
        order_page.order_scooter_full_path(user_data)
        assert order_page.check_order_title()