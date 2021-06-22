'''
Guided Project: "Where Is the Mouse Right Now? p. 443
From ch. 18 in No Starch Press book 'Automate the Boring Stuff with Python" 
--------------------------------------------------------------------------------------------

Writing a program that will constantly display the coordinate position of the mouse, as you move it around.
Thie program can be used to figure out which mouse coordinates you need for GUI automation scripts

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
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: '+ str(y).rjust(4)   # .rjust()will right-justify the strings, so they take up the same amount of space (e.g. if they have 1 or 3 digits)
        print(positionStr, end = '')                                      # 'end', to prevent the default newline character from being added to the end of the printed line.
        print('\b' * len(positionStr), end = '', flush = True)            # To erase the previous position corrdinates, use the \b backspace escape chacater, to erase a character at the end of the current line 
                                                                          # flush = T, calls the print \b backspace characters, otherwise the screen might not update the text as desired.

        # Since the everything within the while loop repeats so quickly, the user won't notice when the cooridnates are updated/change when they move the most

except KeyboardInterrupt:
    print('\nDone.')



