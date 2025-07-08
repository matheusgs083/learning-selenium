from selenium import webdriver
from time import sleep


SITE_URL = "https://www.saucedemo.com/v1/"

driver = webdriver.Edge()

driver.get(SITE_URL)

sleep(5.0)

# full xpath /html/body/div[2]/div[1]/div/div/form/input[3]
# partial xpath //*[@id="login-button"]
