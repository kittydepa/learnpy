i = 0 # The starting point for i
numbers = [] # An empty list, to be added to later on

while i < 6:  # Go through the start/i to 5
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)


"""
A. The same as a function:
numbers = []

def adding (x):
    print(f"Let's move on to the next number in the list {x}")
    numbers.append(x)

    x = x + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom of the list is now {x}")

adding(0)
adding(1)
adding(2)
adding(3)
adding(4)
adding(5)

print("The numbers: ")

for num in numbers:
    print(num)

---------------------------------------------------------

B. The same as a for loop:
numbers = []

for i in range(0, 6):
    print(f"Let's move on to the next number in the list {i}")
    numbers.append(i)

    print("Numbers now: ", numbers)
    print(f"At the bottom of the list is now {i}")

"""
