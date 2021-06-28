'''
Ch. 18 guided project - Automatic Form Filler, from Automate the Boring Stuff.. 1st ed.

What this program will open a Google form (see notes/book for link) and:
    - Click the first text field of the form
    - Move through the form, typing information into each field
    - Click the Submit button
    - Repeat the process with the next set of data

The code will need to do the following:
    - Call pyautogui.click() to click the form and Submit button
    - Call pyautogui.typewrite() to enter text into the fields
    - Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit
'''

## Step 1: Figure out the steps yo