from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from locators import *
from static_data import *
import pytest

def test_enter_cabinet(driver, signin):

    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 5)

    curr_url = driver.current_url
    assert curr_url == url_account

def test_cabinet_to_constructor_by_link(driver, signin):

    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(MainPage.TEXT_CONSTRUCTOR))

    curr_url = driver.current_url
    assert curr_url == url_main

def test_cabinet_to_constructor_by_logo(driver, signin):

    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.LK_BUTTON).click()
    WebDriverWait(driver, 2)
    driver.find_element(*MainPage.BURGER_LOGO).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(MainPage.TEXT_CONSTRUCTOR))

    curr_url = driver.current_url
    assert curr_url == url_main