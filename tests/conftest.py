import pytest
from selenium import webdriver

driver: webdriver.Remote

def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")

    yield # pause and run test

    driver.quit()
