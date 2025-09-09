from selenium.webdriver.common.by import By

class HomePageHeaderLocators: # по вашему замечанию локаторы устойчивые и не используют хрупкие абсолютные пути
    """Локаторы верхней части страницы"""
    logo_yandex = (By.CSS_SELECTOR, '[class*="Header_LogoYandex"]')
    logo_scooter = (By.CSS_SELECTOR, '[class*="Header_LogoScooter"]')
    order_button = (By.XPATH, ".//button[contains(text(), 'Заказать')]")
    order_status_button = (By.XPATH, ".//button[contains(text(), 'Статус заказа')]")
    number_order_field = (By.CSS_SELECTOR, '[class*="Header_Input"]')
    go_button = (By.XPATH, ".//button[contains(text(), 'Go!')]")
    track_field = (By.CSS_SELECTOR, '[placeholder*="номер заказа"]')
    view_button = (By.XPATH, ".//button[contains(text(), 'Посмотреть')]")
    header_page_title = (By.XPATH, ".//div[contains(text(), 'Учебный тренажер')]")

class HomePageLocators:
    """Локаторы основной страницы сервиса"""
    home_page_title = (By.CSS_SELECTOR, '[class*="Home_Header"]')
    order_button = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[contains(text(), 'Заказа')]")
    accept_cookies_button = (By.ID, 'rcc-confirm-button')
    
    # ВОЗВРАЩАЕМ РАБОЧИЙ ЛОКАТОР ДЛЯ ЗАГОЛОВКА ВОПРОСОВ
    questions_title = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Локаторы кнопок вопросов 
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    # Локаторы текста ответов
    questions_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]