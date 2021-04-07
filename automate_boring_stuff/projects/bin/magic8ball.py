import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes, definitely',
    'Reply hazy. Try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
# The line above means: from the list, 'messages', give me the [] indexed value,
# of a random item from the list, anywhere between the first, and 
# total length (minus one cuz that is how you count in Python) of the entire list