'''
My attempt the task
Additional resources: 
    - https://realpython.com/command-line-interfaces-python-argparse/ 

Notes for the task:
    - use module 'argparse' (https://docs.python.org/3/library/argparse.html)

Basically the program needs to use the argparse module to create a command line tool where:
    - it can convert between UUIDs and "device identifiers" (in either order)
    - print the result to the terminal for the user to copy/use
    - have separate flags or subcommands for the 2 required functions
        - (function a = UUID to device identifer
        - (function b = device identifier to UUID)
    - include help text that briefly describes how to use the tool
'''

import argparse

parser = argparse.ArgumentParser(description = "Convert a UUID to device identifier or specify to convert the other way around, with the desired output format indicated by the flag. \n By default, the program will assume the input is a UUID and convert it to a Device ID.")
group = parser.add_mutually_exclusive_group()

# Setting up the flags for the 2 functions the user can choose from, which must be mutually exclusive
group.add_argument("-u", "--uuid", action = "store_true", help = "Convert a Device ID to a UUID")
group.add_argument("-d", "--device", action = "store_true", help = "Convert a UUID to a Device ID")

# Setting up the user input
parser.add_argument("id", type = str, help = "either the UUID or Device ID")

args = parser.parse_args()

# Function that includes both 'a' and 'b', as described earlier
def id_converter(x):
    print("hi {}".format(x))
    # if it starts with (UUID):
    #     then do this crap to it to convert to Device ID
    # elif it starts with (Device ID):
    #     then do this crap to it to conver to UUID
    # else:
    #     print()
    #     sys.exit() # remember to import this!


converter = id_converter(args.id)

#ACTUALLY NO, DISREGARD THESE TWO LINES BELOW
# uuid_result = uuid_converter()
# did_result = did_convert()