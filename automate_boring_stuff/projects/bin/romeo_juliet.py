'''
Quick practice example for downloading web page content and saving it on the hard disk.
From page 239 in 'Automate the Boring Stuff' - No Starch Press
----------------------------------------------------------------------------------------
'''

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status() # Check to see if it was successfull, (any HTTP error?)



# Now we want to save the contents of this web page into a text file. 
# First, create it as an object using open(). Remember that you must use the argument 'wb' for write binary, to preserve the unicode encoding of the text
playFile = open('RomeoAndJuliet.txt', 'wb')



# To 'write' the web page to the file, you can use a for loop with the 'Response' object's iter_content() method like so:
# With this method, it returns each 'chunk'  of content on each itneration through the loop, where each 'chunk' is of the bytes data type, and you specify how many bytes each chunk will containt
# 100000 is usually a good byte size
for chunk in res.iter_content(100000):
    playFile.write(chunk)



# Remember to .close() the file object, so that it saves
playFile.close()



'''
pg. 240 - Review of the process of downloading and saving a file:
    1. Call requests.get() to download the file.
    2. Call open() with 'wb' to create a new file in write binary mode.
    3. Loop over the Response object's inter_content() method.
    4. Call write() on each iteration to write the content to the file.
    5. Call close() to close the file.
'''