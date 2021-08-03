'''
Practice creating a BeautifulSoup object from HTML (p. 245)
From the book 'Automate the Boring Stuff with Python' - No Starch Press
'''
# Run each line separately
import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)


# You can also load an HTML file from your hard drive by passing the 'File' object to bs4.BeautifulSoup()
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)


# From page 247 - enter each line one by one! woo
elems = exampleSoup.select('#author')
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs