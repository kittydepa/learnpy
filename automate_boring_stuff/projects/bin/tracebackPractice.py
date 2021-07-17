import traceback
try:
    raise Exception('This is the error message, you fool.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')



'''
Practice using Python's traceback module
From Ch 10 in 'Automate the Boring Stuff...' No Starch Press
pg. 218


Here, you are creating a txt file, as a log for the Traceback errors, so your program will run without crashing,
and you can refer to the txt tile later for debugging.
'''