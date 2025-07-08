from time import sleep
from selenium import webdriver

driver = webdriver.Edge()

CURRENT_URL = "https://www.saucedemo.com/v1/"

driver.get(CURRENT_URL)

# find_ELEMENT
# username = driver.find_element(by="xpath", value='//*[@id="user-name"]')
# password = driver.find_element(by="xpath", value='//*[@id="password"]')
# loginbotton = driver.find_element(by="xpath", value='//*[@id="login-button"]')

# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# loginbotton.click()

# sleep(2)

#find_ELEMENT(S)

auth_fields = driver.find_elements(by="xpath", value='//*[@class="form_input"]')

print(len(auth_fields))

assert len(auth_fields) == 23, "size error"

sleep(2)


driver.close()