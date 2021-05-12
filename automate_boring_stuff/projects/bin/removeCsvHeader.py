''' 
From 'Automate the Boring Stuff...', page 325

Loop through each CSV file in the directory, and remove the header
'''


import csv, os

os.makedirs('headerRemoved', exist_ok = True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # To do: Read the CSV file in (skipping first row).

    # To do: Write out the new CSV file