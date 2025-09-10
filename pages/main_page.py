import allure
from locators.home_page_locators import HomePageHeaderLocators, HomePageLocators
from pages.base_page import BasePage

class HomePageHeader(BasePage):
    @allure.step('Клик по логотипу Яндекса')
    def yandex_logo_click(self):
        self.click_button(HomePageHeaderLocators.logo_yandex)

    @allure.step('Клик по логотипу Самоката')
    def scooter_logo_click(self):
        self.click_button(HomePageHeaderLocators.logo_scooter)

    @allure.step('Клик по кнопке Заказать')
    def order_button_click(self):
        self.click_button(HomePageHeaderLocators.order_button)

    @allure.step('Клик по кнопке Статус заказа')
    def status_order_click(self):
        self.click_button(HomePageHeaderLocators.order_status_button)

    @allure.step('Заполнение формы номера заказа')
    def send_number_order_to_track_field(self, number):
        self.status_order_click()
        self.send_keys_to_field(HomePageHeaderLocators.number_order_field, number)

    @allure.step('Нажатие на кнопку Go!')
    def go_button_click(self):
        self.click_button(HomePageHeaderLocators.go_button)

    @allure.step('Заполнение формы номера заказа и клик на кнопку Go!')
    def check_order_status(self, number):
        self.status_order_click()
        self.send_number_order_to_track_field(number)
        self.go_button_click()

    @allure.step('Проверка отображения надписи - "Учебный проект"')
    def check_order_title(self):
        return self.check_element(HomePageHeaderLocators.header_page_title)

    @allure.step('Клик по логотипу Яндекс и переход на Dzen')
    def click_yandex_logo_and_go_to_dzen(self):
        original_tab_count = self.get_window_handles_count()
        self.yandex_logo_click()
        self.wait_for_new_tab(original_tab_count)
        self.switch_to_last_tab()
        self.wait_for_domain_in_url('dzen.ru')


class HomePage(BasePage):

    @allure.step('Принять куки')
    def accept_cookie_home_page(self):
        self.click_button(HomePageLocators.accept_cookies_button)

    @allure.step('Скролл и клик на кнопку Заказать')
    def scroll_and_click_on_the_order_button(self):
        self.scroll_to_locator(HomePageLocators.order_button)
        self.click_button(HomePageLocators.order_button)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions(self):
        self.scroll_to_locator(HomePageLocators.questions_title)

    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator): 
        self.scroll_to_questions()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        text_question = self.get_text_locator(question_text_locator)
        return text_question