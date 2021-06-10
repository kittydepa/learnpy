# Reverse Cipher from "Cracking Codes with Python"
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time

# message = 'Three can keep a secret, if two of them are dead.'  
# translated = ''

# i = len(message) - 1
# # print("The len(message) equals ", len(message))  # 49
# # print("len(message) - 1 equals ", i)  # 48
# while i >= 0:
#     translated = translated + message[i]    # Start with the last index value of 'message', hence the backwards-ness 
#   # print('i is', i, ', message[i] is ', message[i], ', translated is', translated)
    
#     i = i - 1                               # Decrementing the variable by 1

# # print(translated)


'''
You can copy the output of this script, and then paste it back into the 'message' variable
to practice decrypting. lol
'''


## Making the program more interesting, by having the 'message' be user input
message = input('Enter message: ')  
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]  
    i = i - 1 

print("Creating your cipher... ")
time.sleep(2)
print("........Loading.........")
time.sleep(2)
print("Here is your cipher: ", translated)
time.sleep(3)