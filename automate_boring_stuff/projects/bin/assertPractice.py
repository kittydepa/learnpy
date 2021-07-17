print('Attempt 1: ')
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The bod bay doors need to be "open".'
if podBayDoorStatus == 'open':
    print('Ran successfully! The pod bay door was open.')

print("------------------------------------------------")

print('Attempt 2: ')
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'Sorry. The pod bay doors need to be "open".'



'''
Practicing using Assertions from Ch 10 in 'Automate the Boring Stuff with Python' No Starch press
'''