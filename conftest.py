import pytest
from selenium import webdriver
from helps.data import app_config

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(app_config.main_page)
    yield driver
    driver.quit()