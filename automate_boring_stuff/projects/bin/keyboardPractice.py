# # To run this program successfully, make sure that you have a text file open in correct location your screen (the click coordinates!)

# import pyautogui
# pyautogui.click(200, 200); pyautogui.typewrite('Hey there friend. \n - Kitty', 0.25)    # (string, duraction between each key stroke)

# # Put both commands on the same line, but separate with a semicolon to ensure that the program runs them separately





# Practice with HotKey combination/function

import pyautogui, time

def commentAfterDelay():
    pyautogui.click(300, 300)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt', '3')

commentAfterDelay()


## Didn't really work for me, but w.e I get the point 
## See page 430 in book for  Review of PyAutoGUI functions