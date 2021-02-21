from sys import argv #imports the ability to use argv

script, filename = argv #stating that we want, script?? file name, and the argv
#arg as in the argumentitive variable

## arg basically means that when you open from the terminal, you will needed
##  to give an input in the name, the very first input needs to be given when opening it!

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">") #why the greater than sign?

txt_again = open(file_again)

print(txt_again.read())
