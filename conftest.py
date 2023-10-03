import pytest
from selenium import webdriver
from locators import *
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def signin(driver):
    def login(url, page):
        driver.get(url)
        driver.find_element(*page).click()
        driver.find_element(*MainPage.NAME_INPUT).send_keys('alaien@yandex.ru')
        driver.find_element(*MainPage.PASSWORD_INPUT).send_keys('Password1789')
        driver.find_element(*MainPage.BUTTON_SIGN_IN).click()

    return login