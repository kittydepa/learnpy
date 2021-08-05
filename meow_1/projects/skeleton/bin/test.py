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

new_id = []
def uuid_converter(id): 
    new_id = []
    if len(id) == 36:
        print("")
        print("You entered the UUID: {}".format(id))
        id_v2 = id.replace("-", "")
        # print(id_v2)
        new_id = id_v2[10:12] + "-" + id_v2[12:18] + "-" + id_v2[18:20] + '-' + id_v2[20:26] + '-' + id_v2[26:32]
        print("Here is the Device ID: {}".format(new_id))
        print("")

    else:
        print("ERROR. Not a valid number of characters.")
        print("HINT: you must include hyphens in between each segment the of UUID or Device ID, and do not include spaces.")


def deviceID_converter(id): 
    new_id = []
    if len(id) == 38:
        print("")
        print("You entered the Device: {}".format(id))
        id_v2 = id.replace("-", "")
        # print(id_v2)
        new_id = id_v2
        print("Here is the UUID: {}".format(new_id))
        print("")

    else:
        print("ERROR. Not a valid number of characters.")
        print("HINT: you must include hyphens in between each segment the of UUID or Device ID, and do not include spaces.")




parser = argparse.ArgumentParser(description = "Convert a UUID to device identifier or specify to convert the other way around, with the desired output format indicated by the flag.")
group = parser.add_mutually_exclusive_group()

# Setting up the flags for the 2 functions the user can choose from, which must be mutually exclusive
group.add_argument("-u", "--uuid", action = "store_const", const = uuid_converter, help = "Convert a Device ID to a UUID")
group.add_argument("-d", "--device", action = "store_const", const = deviceID_converter, help = "Convert a UUID to a Device ID")

# Setting up the user input
parser.add_argument("id", type = str, help = "either the UUID or Device ID")

args = parser.parse_args()
print(type(id))

if args.uuid:
    uuid_converter(id)

elif args.device:
    deviceID_converter(id)

else:
    print("Didn't work. Try again.")
