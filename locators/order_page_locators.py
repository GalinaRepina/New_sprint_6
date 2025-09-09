from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Форма заказа самоката"""
    # Страница 1
    name_field = (By.XPATH, "//input[@placeholder = '* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station_field = (By.CLASS_NAME, 'select-search__input')
    metro = (By.XPATH, "//div[text() = 'Парк культуры']")
    telephone_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text() = 'Далее']")

    # Страница 2
    deliver_order_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.CLASS_NAME, 'Dropdown-arrow')
    rent_period_three_days = (By.XPATH, "//div[text() = 'трое суток']")
    black_color_scooter_check = (By.ID, 'black')
    gray_color_scooter_check = (By.ID, 'grey')
    comment_field = (By.XPATH, "//input[@placeholder= 'Комментарий для курьера']")
    back_button = (By.XPATH, "//button[text() = 'Назад']")
    order_button = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text() = 'Заказать']")

    # Окно подтверждения заказа 
    no_button = (By.XPATH, "//button[text() = 'Нет']")
    yes_button = (By.XPATH, "//button[text() = 'Да']")

    # Окно заказа
    order_placed_text = (By.XPATH, "//div[text() = 'Заказ оформлен']")
    view_status_button = (By.XPATH, "//button[text() = 'Посмотреть статус']")