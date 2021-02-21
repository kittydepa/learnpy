import random

min = 1
max = 20

again = True

while again:
    x = random.randint(min, max)
    print("You rolled a whopping: ")
    print(x)

    if x <= 10:
        print("That sucks.")
    elif x > 10 and x < 16:
        print("Not too shabby.")
    elif x == 20:
        print("DAMN. CRIT HIT! You rolled a natural 20!")
    elif x >= 16:
        print("Niiiice!!!")
    else:
        print("Okay, moving on.")

    another_roll = input('Want to roll again? ')

    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':                             # The lower converts the user input into lower case, to match the condition
        continue
    else:
        break
