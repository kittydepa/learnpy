'''
Practicing web scraping with the webbrowser module
From Ch 11 in 'Automate the Boring Stuff with Python' (p. 234) - No Starch Press


This program will:
    - get a street address from the command line agrugments or the clipboard
    - open the web browser to the Google Maps page for the address
So the code will:
    - read the command line arguments from sys.argv
    - read the clipboard contents
    - call the webbrowser.open() function to open the webbrowser
-----------------------------------------------------------------------------------------
'''

import webbrowser
webbrowser.open('http://inventwithpython.com/')