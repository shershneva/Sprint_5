from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from locators import *
import pytest
@pytest.mark.parametrize("url, element", [
        ("https://stellarburgers.nomoreparties.site/", MainPage.ENTER_BUTTON),
        ("https://stellarburgers.nomoreparties.site/", MainPage.LK_BUTTON),
        ("https://stellarburgers.nomoreparties.site/register", MainPage.HAVE_LOGIN),
        ("https://stellarburgers.nomoreparties.site/forgot-password", MainPage.HAVE_LOGIN)])
def test_user_login(driver, signin, url, element):
    signin(url, element)

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(MainPage.MY_LOGIN))
    login = driver.find_element(*MainPage.MY_LOGIN).get_attribute('value')

    assert login == 'alaien@yandex.ru'


def test_user_logout(driver, signin):
    signin("https://stellarburgers.nomoreparties.site/", MainPage.ENTER_BUTTON)

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(MainPage.BUTTON_EXIT))
    driver.find_element(*MainPage.BUTTON_EXIT).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegistrationPage.SIGNIN_PAGE))
    curr_url = driver.current_url

    assert curr_url == 'https://stellarburgers.nomoreparties.site/login'