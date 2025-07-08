from time import sleep
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/v1/")

print(f"The page title is: {driver.title}")
print(f"The page url is: {driver.current_url}")

with open("html.html", "w") as file: # create a file with a html code
    file.write(driver.page_source)