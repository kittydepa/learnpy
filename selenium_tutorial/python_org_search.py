'''
2.1 Simple Usage from Selenium's Getting Started page https://selenium-python.readthedocs.io/getting-started.html

To make this work:
- Install Selenium :)
- Install Chrome driver
- Allow chromedriver permission to be able to launch this script

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()