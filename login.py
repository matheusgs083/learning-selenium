from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# == configs ==

URL = "https://www.saucedemo.com/v1/"

USER = "standard_user"
PASSWORD = "secret_sauce"

# == driver ==

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get(URL)

# == cod ==

# keys mapping
login_box = driver.find_element(By.XPATH, '//input[@id="user-name"]')
pasword_box = driver.find_element(By.XPATH, '//input[@id="password"]')
login_btn = driver.find_element(By.XPATH, '//input[@id="login-button"]')

login_box.send_keys(USER)
pasword_box.send_keys(PASSWORD)
login_btn.click()

login_confirmation = driver.find_element(By.XPATH, '//*[@id="inventory_filter_container"]/div').is_displayed()

assert login_confirmation, "Login failed!"

## == end ==

sleep(5)
driver.quit()



