# this one is like our scripts with argv
def print_two(*args):  # def, and then function name, then in (), is like the arg parameter
    arg1, arg2 = args  # this line "unpacks" the arguments? but this is not necessary!
    print(f"arg1: {arg1}, arg2 {arg2}")

# the *args above is actually pointless, can just do this instead:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes NO arguments
def print_none():
    print("I got nothin'.")


print_two("Kitty", "Stanca")
print_two_again("Kitty", "Depa")
print_one("First!")
print_none()

# Notes/ function check list
"""
1. Did you start the function with "def"?
2. Does your function have only characters and _ underscore characters?
3. Did you put an open parenthesis right after function name?
4. Did you put your arguments after the parenthesis separated by commas?
5. Did you make each argument unique, i.e. no duplicates?
6. Did you put a close parenthesis and a colon after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more no less.
8. Did you "end" you function by going back to writing with no indent?
"""
