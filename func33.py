numbers = []

def adding (x):
    print(f"Let's move on to the next number in the list {x}")
    numbers.append(x)

    x = x + 1
    #numbers.append(x)
    print("Numbers now: ", numbers)
    print(f"At the bottom of the list is now {x}")

adding(0)
adding(1)
adding(2)

print("The numbers: ")

for num in numbers:
    print(num)
