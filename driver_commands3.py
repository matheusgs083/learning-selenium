from time import sleep
from selenium import webdriver

driver = webdriver.Edge()

CURRENT_URL = "https://leogcarvalho.github.io/test-automation-practice/"

driver.get(CURRENT_URL)

username = driver.find_element(by="xpath", value='//*[@id="username"]')
password = driver.find_element(by="xpath", value='//*[@id="password"]')

login_btn = driver.find_element(by="xpath", value='//*[@id="login-button"]')
login_situation = driver.find_element(by="xpath", value='//*[@id="login-status"]')

assert username.is_displayed(), "The username field is not displayed" # dispplayed in the screen

username.send_keys("admin")
password.send_keys("12345")

login_btn.click()
 
if login_situation.is_displayed:
    print(login_situation.text)

sleep(5.0)