## Password Locker Project- from 'Automate the Boring Stuff with Python'
## Will store account names and their password - insecure

# Step 1 - Store passwords in a data structure, like a dict
passwords = {'email': 'emailpassword123',
             'blog': 'blogpassword123',
             'facebook': 'facebookpassword123'}

# Step 2 - Handling the Command Line Arguments
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first commane line arg is the account name. ... # sys.argv[1] is needs to be able to exectue this script from the command line?

if account in passwords: # Looks in the pass dictuionare for the account name
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.') # if it's there, we get the password
else:
    print('There is no account named' + account) # if not, then told it does not exist in the passwords dict


# To run this program, go to a command prompt and to where the file is stored
# Then enter: 'python pw.py DICTKEY' to get that dict'keys' password