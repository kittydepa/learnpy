'''
From page 322 in 'Automate the Boring Stuff...'
'''

import csv

exampleFile = open('example.csv') # First open the csv file/bring it into the scope
exampleReader = csv.reader(exampleFile) # Make it an object, using csv.reader


# Now fo a for loop, that will bring the line/row number, and its contents
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


# Run this in the terminal