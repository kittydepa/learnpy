'''
Ch 10 - Debugging from 'Automate the Boring Stuff with Python' No Starch Press
Practice Project: Debugging Coin Toss Game
Try to find and fix the bugs so that the program will work correctly.
'''
import logging
import random

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program.')

# ---------------------------------------------------

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input('> ')
    
logging.debug(f'Try 1. Participant guess is: {guess}.')


# Need to convert toss to a string! 
coin_flip = random.randint(0, 1) # 0 is tails, 1 in heads
if coin_flip == 0:
    toss = 'tails'
else:
    toss = 'heads'


logging.debug(f'PRE-randomisation. The toss is: {toss}')
logging.debug('0 is tails, and 1 is heads')


if toss == guess:
    print('You got it!')
    logging.debug(f'POST-randomisation. The toss is: {toss}')

else:
    print('Nope! Guess again!')
    guess = input('> ')
    logging.debug(f'Try 2. Participant guess is: {guess}.')
    logging.debug(f'POST-randomisation. The toss is: {toss}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. Game over.')


'''
Record of Issues:
    1. Always prints as incorrect??? hmm...
    2. Guess is spelled incorrectly the second time.
'''

'''
Notes:
## Check that the while statement works???

x = 'heads'
y = ('heads', 'tails')

if x in y:
    print('yes')  ## It does
else:
    print('no')
'''