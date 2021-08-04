'''
Additional practice with web scraping with Beautiful Soup in Python
From Real Python https://realpython.com/beautiful-soup-web-scraper-python
'''

import requests

URL = "https://realpython.github.io/fake-jobs/" # a static web page
page = requests.get(URL)
page.status_code == requests.codes.ok # to make sure it worked 

print(page.text)