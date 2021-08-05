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

import argparse, sys

new_id = []
def uuid_converter(): 
    new_id = []
    if len(args.uuid) == 36:
        print("")
        print("You entered the UUID: {}".format(args.uuid))
        id_v2 = args.uuid.replace("-", "")
        new_id = id_v2[10:12] + "-" + id_v2[12:18] + "-" + id_v2[18:20] + '-' + id_v2[20:26] + '-' + id_v2[26:32]
        print("Here is the Device ID: {}".format(new_id))
        print("")

    else:
        print("ERROR. Not a valid number of characters.")
        print("HINT: you must include hyphens in between each segment the of UUID or Device ID, and do not include spaces.")


def deviceID_converter(): 
    new_id = []
    if len(args.deviceID) == 26:
        print("")
        print("You entered the Device ID: {}".format(args.deviceID))
        id_v2 = args.deviceID.replace("-", "")
        new_id = ("00000000") + "-" + "00" + id_v2[0:2] + "-" + id_v2[2:6] + "-" + id_v2[6:10] + "-" + id_v2[10:]
        print("Here is the UUID: {}".format(new_id))
        print("")

    else:
        print("ERROR. Not a valid number of characters.")
        print("HINT: you must include hyphens in between each segment the of UUID or Device ID, and do not include spaces.")



# Setting up the user input/top level parser
parser = argparse.ArgumentParser(description = "Convert a UUID to device identifier or specify to convert the other way around, with the desired output format indicated by the flag. Remember to put the flag first, then the ID.")
parser.add_argument("-u", "--uuid", type = str, help = "Convert a UUID to Device ID")
parser.add_argument("-d", "--deviceID", type = str, help = "Convert a Device ID to a UUID")



# # Parse the args and call whatever function was selected
args = parser.parse_args()
print(args)
# print(args.uuid)

if args.uuid is None and args.deviceID is None:
    print("NOOB - you need to enter a UUID or Device ID, with the hyphens '-'.")
elif args.uuid is not None:
    uuid_converter()
elif args.deviceID is not None:
    deviceID_converter()
else:
    sys.exit()


# A practice UUID: 00000000-00A9-4D19-BAF9-99123149DBE9 
# A practice Device ID: E0-010FAB-0A-210521-00010A