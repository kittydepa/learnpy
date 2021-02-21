ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Here is a list of 10 things: ", ten_things)
print("Wait there are not 10 things in that list. Let's fix that...")

stuff = ten_things.split(' ') # AKA split(ten_things) = stuff, so they are individual items
more_stuff = ["Day", "Night", "Song", "Frisbess",
    "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # adds backwards. AKA pop(more_stuff) = next_one
    print("Adding: ", next_one)
    stuff.append(next_one) # AKA append(stuff, next_one) append to stuff, the next 1
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # Prints 2nd item in list
print(stuff[-1]) # Prints corn... the last item???
print(stuff.pop()) # gimme the last item? pop. AKA pop(stuff)
print(' '.join(stuff)) # Adds spaces to stuff? AKA join(stuff, ' ') (Join to stuff, a ' ')
print('#'.join(stuff[3:5])) # Wat, adds # in between 4th and 5th item?
# AKA join(stuff[3:5], '#'). (Join to stuff between the 4th and 5th item, a #)
# Line 23 extracts a 'slice' from stuff. 
