'''
From No Starch Press: 'Automate the Boring Stuff with Python...'
Ch. 18 on Keyboard and Mouse Movement with GUI Automation
'''

import pyautogui
## The following moves the cursor around in a square shape
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration = 0.25)
#     pyautogui.moveTo(200, 100, duration = 0.25)
#     pyautogui.moveTo(200, 200, duration = 0.25)
#     pyautogui.moveTo(100, 200, duration = 0.25)

# Can also use .moveRel, which will move the cursor 'relative' to the latest position of the cursor
for i in range(10):
    pyautogui.moveRel(100, 0, duration = 0.25)
    pyautogui.moveRel(0, 100, duration = 0.25)
    pyautogui.moveRel(-100, 0, duration = 0.25)
    pyautogui.moveRel(0, -100, duration = 0.25)

## How to get the current position of the mouse:
# pyautogui.position()