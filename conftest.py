import pytest
from selenium import webdriver
from locators import *
from static_data import *

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(url_main)
    yield driver
    driver.quit()

@pytest.fixture
def signin(driver):
    driver.get(url_main)
    driver.find_element(*MainPage.ENTER_BUTTON).click()
    driver.find_element(*AuthPage.NAME_INPUT).send_keys(my_login)
    driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(my_password)
    driver.find_element(*AuthPage.BUTTON_SIGN_IN).click()

    return signin