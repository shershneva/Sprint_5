from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from generator import *
from locators import *
import pytest

def test_new_user_registration(driver):
    rnd_username = random_name()
    rnd_email = random_login()
    rnd_password = random_password()

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(AuthPage.REG_LINK))
    driver.find_element(*AuthPage.REG_LINK).click()
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(rnd_username)
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(rnd_email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(rnd_password)
    driver.find_element(*AuthPage.REG_BUTTON).click()

    WebDriverWait(driver, 2).until(EC.presence_of_element_located(AuthPage.BUTTON_SIGN_IN))
    driver.find_element(*AuthPage.NAME_INPUT).send_keys(rnd_email)
    driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(rnd_password)
    driver.find_element(*AuthPage.BUTTON_SIGN_IN).click()

    WebDriverWait(driver, 2).until(EC.presence_of_element_located(MainPage.LK_BUTTON))
    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(AccountPage.MY_LOGIN))
    login = driver.find_element(*AccountPage.MY_LOGIN).get_attribute('value')

    assert login == rnd_email

def test_input_invalid_password(driver):
    rnd_username = random_name()
    rnd_email = random_login()
    invalid_password = '123'

    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(AuthPage.REG_LINK))
    driver.find_element(*AuthPage.REG_LINK).click()
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(rnd_username)
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(rnd_email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(invalid_password)
    driver.find_element(*AuthPage.REG_BUTTON).click()

    error_text = driver.find_element(*RegistrationPage.PASSWORD_ERROR).text
    assert error_text == 'Некорректный пароль'
