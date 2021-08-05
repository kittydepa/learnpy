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
# result = args.id

    
new_id = []


if args.uuid:
    print("")
    print("You entered the UUID: {}".format(id))
    id_v2 = id.replace("-", "")
    # print(id_v2)
    new_id = id_v2[10:12] + "-" + id_v2[12:18] + "-" + id_v2[18:20] + '-' + id_v2[20:26] + '-' + id_v2[26:32]
    print("Here is the Device ID: {}".format(new_id))
    print("")

elif args.device:
    print("This is a Device ID.")

else:
    print("ERROR. Not a valid number of characters.")
    print("HINT: you must include hyphens in between each segment of the UUID or Device ID, and do not include spaces.")


'''
# Or should it be like this????

if arg.uuid:
    print()
if args.device:
    print()

Need to refer to: 
    - https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
'''
