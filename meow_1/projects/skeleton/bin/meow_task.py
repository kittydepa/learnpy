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
import argparse, sys, uuid


# Function for converting a UUID to a Device ID
def uuid_converter(uuid_):
    # First, check if the input is a valid UUID
    def is_valid_uuid(id):
        try:
            uuid.UUID(str(id))
            return True
        except ValueError:
            print("\nERROR: Not a valid UUID!")
            print("HINT: Valid UUIDs must be 32 characters long. You must include hyphens in between each segment of the UUID. Valid UUIDs must follow a specific character structure as well. Did you mean to convert a Device ID to a UUID? If so, use the -d flag instead.\n")
            sys.exit()

    is_valid_uuid(uuid_)
    
    if len(uuid_) == 36:
        print("")
        print("You entered the UUID: {}".format(uuid_))
        id_v2 = uuid_.replace("-", "")
        new_id = id_v2[10:12] + "-" + id_v2[12:18] + "-" + id_v2[18:20] + '-' + id_v2[20:26] + '-' + id_v2[26:32]
        print("Here is the Device ID: {}".format(new_id))
        print("")


def device_id_converter(device_id):
    # Check if it is a valid device ID
    def is_valid_device_id(device_id):
        try:
            len(device_id) == 26
            return True
        except ValueError:
            print("\nERROR: Not a valid number of characters.")
            print("\nHINT: Valid Device IDs must be 26 characters long, and must not include spaces.")
            print("\nDid you mean to convert a UUID to a Device ID? If so, use the -u flag instead.\n")
    
    is_valid_device_id(device_id)

    if is_valid_device_id(device_id) == True:
        print("")
        print("You entered the Device ID: {}".format(args.device_id))
        id_v2 = device_id.replace("-", "")
        id_v3 = ("0000000000") + id_v2
        # print(id_v3)
        # print("Length is: ", len(id_v3))
        new_id = uuid.UUID(id_v3)
        print("Here is the UUID: {}".format(new_id))
        print("")
  
        
# Setting up the user input/top level parser
parser = argparse.ArgumentParser(description = "Convert a UUID to device identifier or specify to convert the other way around, with the desired output format indicated by the flag. Remember to put the flag first, then the ID.")
parser.add_argument("-u", "--uuid", type = str, help = "Convert a UUID to Device ID")
parser.add_argument("-d", "--device-id", type = str, help = "Convert a Device ID to a UUID")

# # Parse the args and call whatever function was selected
args = parser.parse_args()
# print(args)
# print(args.uuid)

if args.uuid is None and args.device_id is None:
    print("NOOB - you need to enter a UUID or Device ID, with the dashes '-'.")
elif args.uuid is not None:
    uuid_converter(args.uuid)
elif args.device_id is not None:
    device_id_converter(args.device_id)
else:
    sys.exit()

# A practice UUID: 00000000-00A9-4D19-BAF9-99123149DBE9
# A practice Device ID: E0-010FAB-0A-210521-00010A