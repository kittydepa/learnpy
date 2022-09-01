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

# Tells which webdriver we are using
driver = webdriver.Chrome()

# Tells which URL to go to
driver.get("http://www.python.org")

# Confirm that the title has "Python" in it
assert "Python" in driver.title

# Read more about find_element, etc.
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Make sure that some results are found, otherwise make the following assertion
assert "No results found." not in driver.page_source

# This will close one tab. You also use .quit to exit the entire browser
driver.close()