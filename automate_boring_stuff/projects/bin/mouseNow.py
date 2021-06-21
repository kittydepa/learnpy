'''
Guided Project: "Where Is the Mouse Right Now?
From ch. 18 in No Starch Press book 'Automate the Boring Stuff with Python" 
--------------------------------------------------------------------------------------------

Writing a program that will constantly display the coordinate position of the mouse, as you move it around.

The code should do the following:
- Call the position() function to obtain the current cooridnates
- Erase the previously printed coordinates as the mouse moves around the screen
- Handle the KeyboardInterrupt exception so the user can pres Ctrl+C to quit

'''

#! python3
#! mouseNow.py = Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')

#TODO: Get and print the mouse coordinates.