from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage: # по вашему замечанию теперь все методы имеют аннотации @allure.step
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента {locator}')
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator) 
        )

    @allure.step('Ожидание присутствия элемента {locator}')
    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Поиск и ожидание локатора {locator}')
    def find_and_wait_locator(self, locator):
        return self.wait_until_visible(locator, timeout=10)

    @allure.step('Клик по элементу {locator}')
    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()

    @allure.step('Ввод текста "{text}" в поле {locator}')
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    @allure.step('Получение текста элемента {locator}')
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    @allure.step('Скролл к элементу {locator}')
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на новую вкладку')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка отображения элемента {locator}')
    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()