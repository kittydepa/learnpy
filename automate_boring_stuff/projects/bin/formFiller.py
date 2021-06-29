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




## Step 1: Figure out the steps and coordinates
'''
See the book, page 432 for the steps needed to fill out the form. Basically, you will need to first click on the first text box of the form, and then you can just press TAB to continue on.
The full steps:
    1. Click the Name field, (you will use mouseNow.py to see and store the coordinates of this in the next step. On MacOS, you may need to click twice)
    2. Type a name and then press TAB
    3. Type a greatest fear and then press TAB
    4. Press the down arrow key the correct number of times to select the answer you want to mark, (e.g., 1x for 'wand', 2x for 'amulet', 3x for 'crystal ball', and 4x for 'money')
       Then press tab. For MacOS you need to press the down arrow key more than once, and on some browsers you may need to press ENTER as well.
    5. Press the right arrow key to select the answer to the RoboCop qusetion. (e.g. Press it once for 2, twice for 3, etc., or just press the spacebar to select 1, which is selected by default. Then press TAB)
    6. Type an additional comment and then press TAB
    7. Press the ENDER key to "click" the Submit button
    8. After submitting the form, the browser will take you to a page where you will need to click a link to return to the form page.
'''

#! python3
# formFiller.py - Automatically fills in the form
import pyautogui, time




## Step 2: With the Google Form open, follow the steps from the book, and run the 'mouseNow.py' script to make note and store the coordinates 
# Enter the correct coordinates for the following:
nameField = (168, 908) 
submitButton = (161, 1793)

# Enter the correct *RGB* colour and coordinate for the following:
submitButtonColour = (130, 130, 130)
submitAnotherLink = (260, 630)




## Step 3: a. Creating the data
# In other cases, this data might be from a csv file or a website, and would require additional code. Here, it we will just use a dict.
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'None'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'I love u.'},
            {'name': 'Alex M.', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocant. Serve the public trust. Uphold the law.'},
           ]
# Add a 0.5 second pause between each function call 
pyautogui.PAUSE = 0.5




## Step 3: b. Start typing the data
for person in formData:
    # Give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColour):
        time.sleep(0.5)

    print('Entering %s info...' %(person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name field
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field
    pyautogui.typewrite(person['fear'] + '\t')




## Step 4: Handle select lists and radio buttons -  Here, we will use the keyboard arrows to select the desired response
    # Fill out the Source of Wizard Power field
    # Note that for this question, it is a drop down menu, that's why we just have the keyboard press down arrow, instead of having to locate EACH response's coordinates
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])
    

    # Fill out the RoboCop field
    # Similarly here, we just have the right arrow to select the response, with the default response being '1', that's why we do not instruct PyAutoGUI to press an arrow key, just a space
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite('right', '\t')
    elif person['robocop'] == 3:
        pyautogui.typewrite('right', 'right', '\t')
    elif person['robocop'] == 4:
        pyautogui.typewrite('right', 'right', 'right', '\t')
    elif person['robocop'] == 5:
        pyautogui.typewrite('right', 'right', 'right', 'right', '\t')




## Step 5: Submit the form and wait
