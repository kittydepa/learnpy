import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target = takeANap)
threadObj.start()

print('End of program.')


'''
When we run this program, we see first, 
'Start of Program.'
'End of Program.'
'Wake up!'

Notice how even though 'End of program.' is the last line of code, it is the second thing to print.
This is because we are storying the function takeANap as another thread - to allow for multithreading to occur.

Because, if we took out the threadObj lines, then the output would follow in the same order as it was written:
So 'Start of program' would first, then takeANap() - which includes waitingn for 5 sec, then print 'Wake Up! 
And then *lastly* printing 'End of program.'

Normally, a program will end when the single thread has ended (e.g., the last line has been executed), but using threadObj.start() opens up a new thread for that functions execution.

Since we *are* using the threadObj, and set the target to tbe the takeANap() function, we can run what comes after that in a diff thread (???)
'''





'''
Ch. 15 pg. 349
Another example, for passing arguments to the thread's target function.
Basically, you MUST use 'args' for arguments that are in the function, and 'kwargs' for the keywords.
'''

# If this is your target function:
print('Cats', 'Dogs', 'Frogs', sep = ' & ')

# This is how you would pass the function in another thread:
import threading
threadObj = threading.Thread(target = print, args = ['Cats', 'Dogs', 'Frogs'], kwargs = {'sep': ' & '})
threadObj.start()