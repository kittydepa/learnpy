## Password Locker Project- from 'Automate the Boring Stuff with Python'
# Will store account names and their password - insecure

passwords = {'email': 'emailpassword123',
             'blog': 'blogpassword123',
             'facebook': 'facebookpassword123'}

# Step 2 - Handling the Command Line Arguments
import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first commane line arg is the account name