'''
Transposition Cipher Decryption
https://www.nostarch.com/crackingcodes/ (BSD Licenced)

How to decrypt a transposition cipher by hand:
    1. Calculate the numer of columns you need by dividing the length of the message by the key, and then rounding up.
    2. Draw boxes in columns and rows. Use the number of columns you calculated in step 1. The no. of rows is the same as the key.
    3. Calculate the no. of boxes to shade in by taking the total no. of boxes (no. of rows * no. of cols) and subtracting the length of the cipher message.
    4. Shade in the no. of boxes you calculated in step 3 at the bottom of the rightmost column.
    5. Fill in the characters of the ciphertext starting at the top row and going from left to right. Skip any of the shaded boxes.
    6. Get the plaintext by reading the leftmost column from top to bottom, and continuing to do the same in each column.
'''