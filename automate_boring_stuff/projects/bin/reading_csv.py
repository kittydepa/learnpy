'''
From page 322 in 'Automate the Boring Stuff...'
'''

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


# Run this in the terminal