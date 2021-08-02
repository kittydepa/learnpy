'''
Quick practice example for downloading web page content and saving it on the hard disk
From page 239 in 'Automate the Boring Stuff' - No Starch Press
'''

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status() # Check to see if it was successfull, (any HTTP error?)

# Now we want to save the contents of this web page into a text file. 
# First, create it as an object using open(). Remember that you must use the argument 'wb' for write binary, to preserve the unicode encoding of the text
playFile = open('RomeoAndJuliet.txt', wb)