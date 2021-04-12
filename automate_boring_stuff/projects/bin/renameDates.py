'''From ch 9. in Automate the Boring Stuff
Will make a script that will rename files that have a US-style
date to European-style date. 

The program will:
- Search all filenames in the cd for US-style dates
- When one is found, rename it with date changed to EU style

Which in turn means that the program will:
- Create a regex that can find US-style dates
- Call on os.listdir() to find all the files in the cd
- Loop over each filename, using the regex to check if there is a date
- If it does, rename the file using shutil.move()
'''

## Step 1: Create a Regex for American-Style Dates
import shutil, os, re

# Create a regex object that matches US dates
datePattern = re.compile(r"""^(.*?) # all dext before the date
    ((0|1)?\d)- # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two difits for the date
    ((19|20)\d\d) # four digits for the year
    (.*?)$ # match any text that comes after the date
    """, re.VERBOSE) # VERBOSE will allow whitespace and comment sin the regex string to make it more readable


## Step 2: Identify the Date Parts from the Filenames
# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename...The numbers related to regex expression above
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TO DO: Skip files without a date.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
# TO DO: Get the different parts of the filename.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)  


# Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


# Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)


# Rename the files.
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
#shutil.move(amerFilename, euroFilename) # uncoment after testing