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

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90)) # Generate a random Uppercase letter (based on ASCII code??)

lowercaseLetter1 = chr(random.randint(97, 122)) # based on ASCII
lowercaseLetter2 = chr(random.randint(97, 122))

digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))

punctuation1 = chr(random.randint(33, 39))
punctuation2 = chr(random.randint(33, 39))

#print(password)

# Now we need to shuffle, make a function that shuffles
def shuffle(x):
    tempList = list(x)
    random.shuffle(tempList)
    return ''.join(tempList) # Why do we need this part/why is it written like this?


# The 'formula' for what makes up a password
password = (uppercaseLetter1 + lowercaseLetter1 + digit1 + punctuation1 + uppercaseLetter2 + lowercaseLetter2 + digit2 + punctuation2)

# Appling the shuffle function to our password formula
password = shuffle(password)

# Printing the output
print(password)
