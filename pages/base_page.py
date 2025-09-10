from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
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

    @allure.step('Ожидание кликабельности элемента {locator}')
    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Поиск и ожидание локатора {locator}')
    def find_and_wait_locator(self, locator):
        return self.wait_until_visible(locator, timeout=10)

    @allure.step('Клик по элементу {locator}')
    def click_button(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    @allure.step('Ввод текста "{text}" в поле {locator}')
    def send_keys_to_field(self, locator, text):
        element = self.find_and_wait_locator(locator)
        element.clear()
        element.send_keys(text)

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

    @allure.step('Получение количества открытых вкладок')
    def get_window_handles_count(self):
        return len(self.driver.window_handles)

    @allure.step('Ожидание открытия новой вкладки')
    def wait_for_new_tab(self, original_tab_count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > original_tab_count
        )

    @allure.step('Переключение на последнюю вкладку')
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание загрузки страницы с доменом {domain}')
    def wait_for_domain_in_url(self, domain, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: domain in d.current_url
        )

    @allure.step('Ожидание текста в элементе {locator}')
    def wait_for_text_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step('Ожидание изменения URL')
    def wait_for_url_change(self, original_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != original_url
        )