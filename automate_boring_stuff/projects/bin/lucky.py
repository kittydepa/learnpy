'''
Project "I'm Feeling Luck Google Search" from 'Automate the Boring Stuff with Python' No Starch Press

This program will:
    - Get search keywords from the command line arugments
    - Retrieve the search results page
    - Open a browser tab for each result

The code will do the following:
    - Read the command line arguments from 'sys.argv'
    - Fetch the search result page with the 'requests' module
    - Find the links to each search result
    - Call the 'webbrowser.open()' function to open the web browser
'''



import requests, sys, webbrowser, bs4
# requests - to downloaded the search result page. BeautifulSoup to find the search result links in the HTML. webbrowser to open those links in browser tabs.



## Step 1: Get the command line arguments and request the search page
print('Googling...') # Display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()



## Step 2: Find all the results




## Step 3: Open web browsers for each result