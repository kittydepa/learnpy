'''
My attempt at the task
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

Note about UUID and Device ID:
    - UUIDs are made of 32 hexidecimal values, total
        - they have 5 segments where seg1 has 8 values, seg2: 4, seg3: 4, seg4:4, and seg5:12
        - are NOT case sensistive
    - Device IDs are made of 22 total (- the first 10 of the UUID)
        - also have 5 segments where seg 1 has 2 values, seg2:6, seg3:2, seg4:6, and seg5: 6
        - ARE case sensitive
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
def id_converter(id): # where ex would be args.id (?)
    new_id = []
    if len(id) == 36:
        print("this is a UUID.")
        new_id = "something"
        print(new_id)

    elif len(id) == 26:
        print("This is a Device ID.")

    else:
        print("ERROR. Not a valid number of characters.")
        print("HINT: you must include hyphens in between each segment the UUID or Device ID, and do not include spaces.")



    #print("hi {}".format(x))
    # if it starts with (UUID):
    #     then do this crap to it to convert to Device ID
    # elif it starts with (Device ID):
    #     then do this crap to it to conver to UUID
    # else:
    #     print()
    #     sys.exit() # remember to import this!


converter = id_converter(args.id)

'''
# Or should it be like this????

if arg.uuid:
    print()
if args.device:
    print()

Need to refer to: 
    - https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
'''

#ACTUALLY NO, DISREGARD THESE TWO LINES BELOW
# uuid_result = uuid_converter()
# did_result = did_convert()