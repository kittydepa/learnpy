# Caeser Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip, time

# The string to be encryped/decrypted
message = input('Enter a message you would like to encrypt: ')

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = 'encrypt' # Set this to either 'encrypt' or ' decrypt

# Every possible symbol that can be encrypter:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' # In cryptography a symbol set is every possible symbol a cipher could contain

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex -len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print("Creating your message...")
time.sleep(2)
print("........Loading........")
time.sleep(2)
print("Ready! Here it is: ")
time.sleep(2)
print("This is the message encrypted: ", translated)
time.sleep(0.5)
print("This is the original message: ", message)
pyperclip.copy(translated) # this like will automatically copy the encrypted message to the clipboard on your computer
time.sleep(2)
print("Thanks for participating.")
time.sleep(2)


## NOTE TO SELF: Edit the script so that it will ask the user/at the command line if they would first like to encryp ot decrypt
