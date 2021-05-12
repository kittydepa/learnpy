''' 
From 'Automate the Boring Stuff...', page 325

Loop through each CSV file in the directory, and remove the header
'''


import csv, os

# Step 1: Loop through each CSV file
os.makedirs('headerRemoved', exist_ok = True) # This makes a folder called 'headerRemoved', where all the head-less CSVs will be written

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...') # Just so we know that stuffs is happenings




# Step 2:  Read in the CSV file (skipping the 1st row)... this is part of the above for loop
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:  # but why is this not a 0?
            continue # skip the first row. line_num means row number. This will be false for every row after, hence copying everything BUT the header to the new csv file
        csvRows.append(row)
    csvFileObj.close() # save it




# Step 3: Now we need to write out the result of the for-loops writen above into a new CSV file
        # Write out the csv file
csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline = '')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()