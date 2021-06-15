# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = 'Common sense is not so common'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in the ciphertext to the screen with a | (pipe character) after it in case there are spaces at the end of it
    print(ciphertext + '|')

    # Copy the encrypted string in the ciphertext to the clipboard:
    pyperclip.copy(ciphertext)



# The function that actually does the encrypting:
def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key 

    # Loop through each column in ciphertext// adding text to each string along the columns
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at the currentIndex in message at the end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)


# If this file is run (instead of imported as a module), call the main() function:
if __name__ == '__main__':
    main()



## Note: every time a function is called, a *local scope* is created!
## Variables that are created during a function call exist in the local scope, and are called 'local variables'
## When the function returns, the local scope is destroyed
## Otherwise, variables outside of a function are global