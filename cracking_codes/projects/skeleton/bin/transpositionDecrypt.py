'''
Transposition Cipher Decryption
https://www.nostarch.com/crackingcodes/ (BSD Licenced)

How to decrypt a transposition cipher by hand:
    1. Calculate the number of columns you need by dividing the length of the message by the key, and then rounding up.
    2. Draw boxes in columns and rows. Use the number of columns you calculated in step 1. The no. of rows is the same as the key.
    3. Calculate the no. of boxes to shade in by taking the total no. of boxes (no. of rows * no. of cols) and subtracting the length of the cipher message.
    4. Shade in the no. of boxes you calculated in step 3 at the bottom of the rightmost column.
    5. Fill in the characters of the ciphertext starting at the top row and going from left to right. Skip any of the shaded boxes.
    6. Get the plaintext by reading the leftmost column from top to bottom, and continuing to do the same in each column.
'''

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio s s c'  # Your encrypted message here
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | after it, in case there are spaces at the end of the decrypted message:
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and "rows" of the grid that the plaintext is wrriten on by
    # using a list of string. First, we need to calculate a few values.

    # The no. of columns in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The no. of rows in our grid:
    numOfRows = key
    # The no. of 'shaded boxes' in the last column of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column

        # If there are no more columns OR we are at a shaded box, go back to the first column and the next row
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module), call the main() functoin
if __name__ == '__main__':
    main()