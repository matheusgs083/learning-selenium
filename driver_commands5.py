from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge()

CURRENT_URL = "https://www.hyrtutorials.com/p/waits-demo.html"

driver.get(CURRENT_URL)
driver.implicitly_wait(11)
wait = wc()

# add_text = driver.find_element(by="xpath", value='//*[@id="btn1"]').click()

# textbox = driver.find_element(by="xpath", value='//*[@id="txt1"]')

# assert textbox.is_displayed(), "textbox notfound"

# textbox.send_keys("Ficha")

add_text = driver.find_element(by="xpath", value='//*[@id="btn1"]').click()


wait = (driver, 10)
textbox = driver.find_element(by="xpath", value='//*[@id="txt1"]')

sleep(2)