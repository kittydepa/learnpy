'''
PRACTICE/TRYING THINGS OUT
Additional resources: 
    - https://realpython.com/command-line-interfaces-python-argparse/ 

Notes for the task:
    - use module 'argparse' (https://docs.python.org/3/library/argparse.html)
'''

# # Here is an implementation of a command line interface WITHOUT using the 'argparse' library
# # The program will take a command line input and 'ls' list that directory
# import os, sys

# if len(sys.argv) > 2:
#     print('You have specified too many arguments.')
#     sys.exit()

# if len(sys.argv) < 2:
#     print('You need to specify the path to be listed.')
#     sys.exit()

# input_path = sys.argv[1]

# if not os.path.isdir(input_path):
#     print('The path specified does not exist.')
#     sys.exit()

# print('\n'.join(os.listdir(input_path)))

# -------------------------------------------------------------------------------

# # How the code above can be improved using 'argparse'
# import argparse
# import os, sys

# # Create the parser
# my_parser = argparse.ArgumentParser(description = 'List the content of a folder')

# # Add the arguments
# my_parser.add_argument('Path',
#                        metavar = 'path',
#                        type = str,
#                        help = 'the path to the list')

# # Execute the parse_args() method
# args = my_parser.parse_args()

# input_path = args.Path

# if not os.path.isdir(input_path):
#     print('The path specified does not exist.')
#     sys.exit()

# print('\n'.join(os.listdir(input_path)))



# -------------------------------------------------------------------------------



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help = "increase output verbosity", action = "store_true")

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
