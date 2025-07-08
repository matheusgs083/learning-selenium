from time import sleep
from selenium import webdriver


URL = "https://www.saucedemo.com/v1/"
URL_NEW_PAGE = "https://github.com/matheusgs083/learning-selenium"
PAUSE_TIME = 2.0

driver = webdriver.Edge()

# get 
driver.get(URL)

#maximaze_window
driver.maximize_window()

# refresh
sleep(PAUSE_TIME)
driver.refresh()

# new page
driver.get(URL_NEW_PAGE)
sleep(PAUSE_TIME)

# back
driver.back()
sleep(PAUSE_TIME)

# forward
driver.forward()
sleep(PAUSE_TIME)

# switch to
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
sleep(PAUSE_TIME)

# close = close page
driver.close()
sleep.close()

# quit = close process
driver.quit()