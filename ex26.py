print("How old are you?", end=' ') # If you take away the end, just prompts on the next line rather than the same line.
age = input()
print("How tall are you?", end=' ')
height = input() # added this line
print("How much do you weigh?", end=' ') # Missing parenthesis here
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv
script, filename = argv # ???? Wtf was this again. See above, need to import?

txt = open(filename) # There was a typo here

print(f"Here's your file {filename}:") # Need to add the 'f' for functions
print(txt.read()) # A typo here?

print("Type the filename again:")
file_again = input("> ") # Dont look right...

txt_again = open(file_again)

print(txt_again.read()) # It replaced second _ with a .


print("Let\'s practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # Added a quote mark here
print(poem)
print("--------------") # Added a quote mark here


five = 10 - 2 + 2 # Fixed math here
print(f"This should be five: {five}") # Added a closing parenthesis

def secret_formula(started): # Added a colon here
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # Added math operator sign (division?)
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # Added an underscore
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
# Error on line 66...change to just 'formula', because calling on what was stated
# In the line above omg


people = 20
cats = 30 # Typo
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # Added parenthesis

if people > cats: # Changed to greater than sign
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # Added a colon
    print("The world is dry!")


dogs == 5 # Changed to ==, because += does not make sense here?

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # Added a colon
    print("People are less than or equal to dogs.") # Added a quote mark


if people == dogs: # Added another equals sign
    print("People are dogs.")
