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
url = 'http://google.com/search?q=' + ' '.join(sys.argv[1:])
print(url)
res = requests.get(url)
res.raise_for_status()
#print(res.text)
# with open("./wtf.html", "w") as f:
#     f.write(res.text)
# sys.exit()


## Step 2: Find all the results
# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('a') 
# based on the inpsecting relement, it seems like there is a class "r" used for the search results
# The above will find all <a> elements that are within an element that has the "r" CSS class
print(linkElems)


## Step 3: Open web browsers for each result (the first 5 results)
numOpen = min(5, len(linkElems)) # min will pull up the smallest of the integer or float arguments it passes
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))