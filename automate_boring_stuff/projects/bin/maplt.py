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
#! python3
#! mapIt.py - Launched a map in the browser using an address from the command line or clipboard


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])  # This stores a list of the program's file name and command arguments, and since you don't want the program file name, you use [1:] to skip over that argument

else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)