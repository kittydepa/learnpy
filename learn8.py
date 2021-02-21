formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # puts line 1 in here 4 times
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


#formatter.format() - is it the same as doin f"String goes here"?
#ANSWER - no, format() just lets you put past in the {} whatever you have defined as
# format() or something like that

# For more info see: https://www.geeksforgeeks.org/python-format-function/#:~:text=str.,a%20string%20through%20positional%20formatting.
