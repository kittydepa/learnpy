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
# parser.add_argument("-v", "--verbose", help = "increase output verbosity", action = "store_true")

# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# parser.add_argument("square", type = int,
#                     help = "display a square of a given number")
# parser.add_argument("-v", "--verbose", action = "store_true",
#                     help = "increase output verbosity")
# args = parser.parse_args()
# answer = args.square ** 2

# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)
# Note that for the above, the order doesn't matter, so the user can enter into the command line e.g., "-v 3" or, "--verbose 3", "3 -v" etc.




# ## Making the program handle multiple verbosity values!
# parser.add_argument("square", type = int,
#                     help = "display a square of a given number")
# parser.add_argument("-v", "--verbosity", type = int, choices = [0, 1, 2], # int for the different versions the user can request to choose from for the output
#                     help = "increase output verbosity")
# args = parser.parse_args()
# answer = args.square ** 2

# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



## Now will use verbosity levels to display *more* text, instead of just *changing* the text
parser.add_argument("x", type = int, help = "the base")
parser.add_argument("y", type = int, help = "the exponent")
parser.add_argument("-v", "--verbosity", action = "count", default = 0)

args = parser.parse_args()
answer = args.x ** args.y

if args.verbosity >= 2:
    print("Running '{}'".format(__file__))
if args.verbosity >= 1:
    print("{}^{} == ".format(args.x, args.y), end = "")

print(answer)