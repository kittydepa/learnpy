'''
Practicing Opening Files with Default Applications in Python
See ch. 15, pg. 355 in 'Automate the Boring Stuff with Python', No Starch Press
'''

fileObj = open('hej.txt', 'w')
fileObj.write('Hello there friend!')

import subprocess
subprocess.Popen(['start', 'hej.txt'], shell = True)