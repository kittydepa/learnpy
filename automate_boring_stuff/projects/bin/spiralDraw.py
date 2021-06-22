'''
Guided Project: Practicing dragging the mouse, in a a drawing app - p. 421
From ch. 18 in No Starch Press book 'Automate the Boring Stuff with Python" 
'''

import pyautogui, time

time.sleep(5)        # a 5 second delay so that you can move the mouse cursor over the drawing program's window with the Pencil or Brush tool selected
pyautogui.click()    # click to put drawing program in focus// A window is in focus when it has an active blinking cursor. Whereever you click, that's where the cursor will start to draw/drag
distance = 500 # the pixel length/ AKA brushstroke length is X pixels

while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.2)    # move right
    distance = distance - 10   # - 10 here means by 10 pixels
    pyautogui.dragRel(0, distance, duration = 0.2)    # move down
    pyautogui.dragRel(-distance, 0, duration = 0.2)   # move left
    distance = distance - 10
    pyautogui.dragRel(0, -distance, duration = 0.2)   # move up