'''
Guided Project: "Where Is the Mouse Right Now? p. 443
From ch. 18 in No Starch Press book 'Automate the Boring Stuff with Python" 
--------------------------------------------------------------------------------------------

Writing a program that will constantly display the coordinate position of the mouse, as you move it around.

The code should do the following:
- Call the position() function to obtain the current cooridnates
- Erase the previously printed coordinates as the mouse moves around the screen
- Handle the KeyboardInterrupt exception so the user can pres Ctrl+C to quit

'''
## Step 1: Import the module
#! python3
#! mouseNow.py = Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.') # See further down, that when a user does this, this should catch the 'KeyboardInterrupt' exception



## Step 2: Set up the 'quit code' and infinite loop (to constantly print the coordinates of the mouse's position)
try:
    while True:
        # Get and print mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: '+ str(y).rjust(4)

except KeyboardInterrupt:
    print('\nDone.')



## Step 3: Get and print the mouse coordinates