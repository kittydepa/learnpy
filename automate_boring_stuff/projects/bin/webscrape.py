'''
Additional practice with web scraping with Beautiful Soup in Python
From Real Python https://realpython.com/beautiful-soup-web-scraper-python
'''

import requests
from bs4 import BeautifulSoup



URL = "https://realpython.github.io/fake-jobs/" # a static web page
page = requests.get(URL)
# page.status_code == requests.codes.ok # to make sure it worked 
# print(page.text)



# Finding Elements by ID
soup = BeautifulSoup(page.content, "html.parser") # Need to pass .content instead of .text to avoid problems with character encoding. The 2nd argument ensures you use the right parser for HTML
results = soup.find(id = "ResultsContainer")
print(results.prettify())



# Finding Elements by class