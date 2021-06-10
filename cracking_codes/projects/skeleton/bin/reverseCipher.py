# Reverse Cipher from "Cracking Codes with Python"
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'Three can keep a secret, if two of them are dead.'  
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

'''
You can copy the output of this script, and then paste it back into the 'message' variable
to practice decrypting. lol
'''