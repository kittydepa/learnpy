"""
From ch 15 of 'Automate the Boring Stuff'
Super Stopwatch Project: Will track amount of time has gone by
between presses of the ENTER key, with each key press = 1 'lap' on the timer.
Will print the lap #, the total time, and lap time.
"""

import time

# Display program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. \nPress Ctrl-C to quit.')
input()                # pressing Enter to begin
print('Started.')

startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try: # to prevent from crashing, wrap it in a try-statement 
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end = '')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')