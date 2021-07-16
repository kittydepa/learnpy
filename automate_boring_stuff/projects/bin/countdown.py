'''
Guided project: Simple countdown program.
Ch 15 in 'Automate the Boring Stuff with Python' No Starch Press

Writing a simple countdown program that will play an alarm sound at the end of the countdown


At a high level, the program will:
    - Count down from 60
    - Play the sound file (alarm.wav) when the countdown reaches 0

The code will then need to:
    - Pause for 1 second in between displaying each number in the coundown, by calling time.sleep()
    - Call subprocess.Popen() to open the sound file with the default application

----------------------------------------------------------------------------------------------------------------
'''

#! python3
#! countdown.py - A simple countdown script.

import time, subprocess

## Step 1: Count down
timeLeft = 10                     # This will hold the numer of seconds left in the countdown, starting with 60 sec
while timeLeft > 0:
    print('Time left in countdown = ', timeLeft)
    print(end = '')
    time.sleep(1)
    timeLeft = timeLeft - 1



## Step 2: Play the sound file at the end of the countdown
subprocess.Popen(['start', 'alarm.wav'], shell = True)

'''
Alternatively, you could also use Popen() to open/create a pop-up window,
with a text file, that says something like 'Break time is over!'
'''