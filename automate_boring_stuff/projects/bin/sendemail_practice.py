"""
Sending Email example from Ch 16 - Automate the Boring Stuff with Python
Note: This example will not work, as the emails and passwords are just placeholders
"""

import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587) # The name of the domain for the email service you use, and the port number (usually 587, but might be 465 otherwise)
smtpObj.ehlo() # This says "hello" to the email server. Need to do this to make sure you established a connection to the server

smtpObj.starttls()
smtpObj.login('bob@example.com', 'my_secret_password')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long. \n Dear Alice, so long. Sincerely, Bob')
smtpObj.quit()