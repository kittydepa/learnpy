import random

try:
    min = int(input('Enter the minimum value of the die: '))
    max = int(input('Enter the maximum value of the die: '))
except:
    print('Input invalid. Program will revert to defaults.')
    min = 1
    max = 6

again = True

while again:
    print(random.randint(min, max))

    another_roll = input('Want to roll again? ')

    if another_roll() == 'yes' or another_roll() == 'y':
        continue
    else:
        break
