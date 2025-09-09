import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя: {text}')
    def send_name_to_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.name_field, text)

    @allure.step('Заполнение поля Фамилия: {text}')
    def send_last_name_to_last_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.last_name_field, text)

    @allure.step('Заполнение поля Адрес: {text}')
    def send_address_to_address_field(self, text):
        self.send_keys_to_field(OrderPageLocators.address_field, text)

    @allure.step('Заполнение поля Станция метро: {text}')
    def send_metro_station_to_metro_station_field(self, text):
        self.click_button(OrderPageLocators.metro_station_field)
        self.send_keys_to_field(OrderPageLocators.metro_station_field, text)
        self.click_button(OrderPageLocators.metro)

    @allure.step('Заполнение поля Телефон: {text}')
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys_to_field(OrderPageLocators.telephone_field, text)

    @allure.step('Клик на кнопку Далее')
    def click_on_the_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполнение поля Когда привезти заказ: {text}')
    def send_deliver_to_deliver_order_field(self, text):
        self.click_button(OrderPageLocators.deliver_order_field)
        self.send_keys_to_field(OrderPageLocators.deliver_order_field, text)

    @allure.step('Выбор срока аренды')
    def period_time(self):
        self.click_button(OrderPageLocators.rent_period_field)
        self.click_button(OrderPageLocators.rent_period_three_days)

    @allure.step('Выбор цвета самоката')
    def select_color_scooter(self):
        self.click_button(OrderPageLocators.black_color_scooter_check)

    @allure.step('Заполнение поля Комментарий: {text}')
    def send_comment_to_comment_field(self, text):
        self.send_keys_to_field(OrderPageLocators.comment_field, text)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('Клик на кнопку Да для подтверждения заказа')
    def confirm_order_scooter(self):
        self.click_button(OrderPageLocators.yes_button)

    @allure.step('Заполнение данных на странице "Для кого самокат"')
    def complete_filling_of_the_who_is_scooter_form(self, user):
        self.send_name_to_name_field(user['first_name'])
        self.send_last_name_to_last_name_field(user['last_name'])
        self.send_address_to_address_field(user['address'])
        self.send_metro_station_to_metro_station_field(user['metro_station'])
        self.send_telephone_number_to_telephone_number_field(user['phone'])
        self.click_on_the_next_button()

    @allure.step('Заполнение данных на странице "Про аренду"')
    def complete_filling_of_the_about_rent_form(self, user):
        self.send_deliver_to_deliver_order_field(user['delivery_date'])
        self.period_time()
        self.select_color_scooter()
        self.send_comment_to_comment_field(user['comment'])
        self.click_order_button()

    @allure.step('Полное оформление заказа самоката для пользователя')
    def order_scooter_full_path(self, user):
        self.complete_filling_of_the_who_is_scooter_form(user) 
        self.complete_filling_of_the_about_rent_form(user)
        self.confirm_order_scooter()

    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.order_placed_text).is_displayed()