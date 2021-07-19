'''
Ch 10 - Debugging from 'Automate the Boring Stuff with Python' No Starch Press
Practice Project: Debugging Coin Toss Game
Try to find and fix the bugs so that the program will work correctly.
'''

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input('> ')
toss = random.randint(0, 1) # 0 is tails, 1 in heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input('> ')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. Game over.')