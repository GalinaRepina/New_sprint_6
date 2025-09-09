import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from helps.data import FAQData, app_config
from locators.home_page_locators import HomePageLocators
from pages.main_page import HomePage, HomePageHeader

class TestMainPage:

    @allure.title('Тест проверки перехода на главную страницу веб-приложения по клику на логотип "Самокат"')
    @allure.description('''1)Кликаем на кнопку "Заказать"
2)Кликаем на логотип "Самокат"
3)Сравниваем текущий URL с ожидаемым и отображение надписи - "Учебный проект"''')
    def test_scooter_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        home_page = HomePage(driver)
        home_page.accept_cookie_home_page()
        header_page.order_button_click()
        header_page.scooter_logo_click()
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()
        assert current_url == app_config.main_page and title_is_displayed

    @allure.title('Тест проверки перехода на Dzen по клику на логотип Яндекс')
    @allure.description('''1)Кликаем на логотип Яндекс
2)Переключаемся на новую вкладку
3)Проверяем загрузку Dzen по домену''')
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        home_page = HomePage(driver)
        home_page.accept_cookie_home_page()
        
        # Запоминаем текущее количество вкладок
        original_windows = driver.window_handles
        
        header_page.yandex_logo_click()
        
        # Ждем открытия новой вкладки
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > len(original_windows)
        )
        
        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        
        # Ждем загрузки страницы и редиректа на dzen
        WebDriverWait(driver, 15).until(
            lambda d: 'dzen.ru' in d.current_url or 'yandex.ru' in d.current_url
        )
        
        current_url = driver.current_url
        # Проверяем что мы на домене dzen.ru или прошли через yandex аутентификацию
        assert 'dzen.ru' in current_url or 'yandex.ru' in current_url

    @allure.title('Тест проверки текста ответов на вопросы')
    @allure.description('''1)Скроллим до блока с вопросами;
2)Кликаем на вопрос;
3)Проверяем текст ответа''')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text',
                             zip(HomePageLocators.questions, HomePageLocators.questions_text, FAQData.EXPECTED_ANSWERS))
    def test_accordeon(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePage(driver)
        home_page.accept_cookie_home_page()
        text = home_page.get_text_question(question_locator, question_text_locator)
        assert text == expected_question_text