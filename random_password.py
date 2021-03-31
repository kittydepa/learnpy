# https://www.101computing.net/random-password-generator/
# password, with 8 characters, that must also include:
'''
2 uppercase letters from A to Z
2 lowercase letters from a to z
2 digits from 0 to 9
2 punctuation signs such as !, ?, ", #, etc."
'''
# Will use ASCII for this https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf

import random

uppercaseLetter = chr(random.rantint(65, 90)) # Generate a random Uppercase letter (based on ASCII code??)
lowercaseLetter = chr(random.randint(97, 122)) # based on ASCII
digit = chr(random.randint(48, 57))
punctuation = chr(random.randint(33, 152))
