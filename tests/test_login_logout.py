from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from locators import *
import pytest

@pytest.mark.parametrize("url, element", [
        ("https://stellarburgers.nomoreparties.site/", MainPage.ENTER_BUTTON),
        ("https://stellarburgers.nomoreparties.site/", MainPage.LK_BUTTON),
        ("https://stellarburgers.nomoreparties.site/register", AuthPage.HAVE_LOGIN),
        ("https://stellarburgers.nomoreparties.site/forgot-password", AuthPage.HAVE_LOGIN)])
def test_user_login(driver, url, element):
    driver.get(url)
    driver.find_element(*element).click()
    driver.find_element(*AuthPage.NAME_INPUT).send_keys(my_login)
    driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(my_password)
    driver.find_element(*AuthPage.BUTTON_SIGN_IN).click()

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(AccountPage.MY_LOGIN))
    login = driver.find_element(*AccountPage.MY_LOGIN).get_attribute('value')

    assert login == my_login

def test_user_logout(driver, signin):

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(AccountPage.BUTTON_EXIT))
    driver.find_element(*AccountPage.BUTTON_EXIT).click()
    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(AuthPage.BUTTON_SIGN_IN))
    button_text = driver.find_element(*AuthPage.BUTTON_SIGN_IN).text

    assert button_text == 'Войти'
