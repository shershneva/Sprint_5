from selenium.webdriver.support.ui import WebDriverWait
from conftest import *
from locators import *
import pytest

@pytest.mark.parametrize('tab1, tab2', [(MainPage.SAUCES, MainPage.BREAD), (MainPage.FILLING, MainPage.SAUCES), (MainPage.SAUCES, MainPage.FILLING)])
def test_constructor_current_tab(driver, tab1, tab2):
    driver.get(url_main)
    WebDriverWait(driver, 5)
    driver.find_element(*tab1).click()
    active_tab = driver.find_element(*tab2)
    active_tab.click()
    WebDriverWait(driver, 5)
    tab_class = active_tab.get_attribute('class')

    assert 'current' in tab_class