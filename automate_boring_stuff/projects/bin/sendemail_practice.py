"""
Sending Email example from Ch 16 - Automate the Boring Stuff with Python
Note: This example will not work, as the emails and passwords are just placeholders
"""

import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()

smtpObj.starttls()
smtpObj.login('bob@example.com', 'my_secret_password')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long. \n Dear Alice, so long. Sincerely, Bob')
smtpObj.quit()