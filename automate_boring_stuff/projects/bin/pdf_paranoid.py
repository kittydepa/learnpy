''' 
Project from pg. 316 in Automate the Boring Stuff

-------------------------------------------------------------------------

PART 1

Using os.walk(), write a script that will:
a. go through every PDF in a folder & its subfolders (p. 198?)
b. encrypt each of the PDFs using a pw given in the command line
c. save each encrypted pdf with _encrypted.pdf suffic

Before deleting the original PDF file have the program attempt to 
read and decrypt the file, to make sure it was encrypted correctly.

-------------------------------------------------------------------------

PART 2

Write a program that:
a. finds all encrypted PDFs in a folder & its subfolders
b. and create a decrypted copy of the PDF using a provided pw
c. if the pw is incorrect, the program should print a message to
  the user and continue to the next PDF

-------------------------------------------------------------------------
'''

## PART 1 
# a. 

import shutil, os
import PyPDF2
from PyPDF2.pagerange import parse_filename_page_ranges

for folderName, subfolder, filenames in os.walk(r'C:\\Users\\Kitty\\Desktop\\learnpy\\automate_boring_stuff\\projects\\bin'):
    if '.pdf' in filenames:
        for pageNum in filenames:
            pdfFile = open('filenames.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
        
        print('Give a password: ')
        pdfWriter.encrypt(input('> '))
        resultPdf = open(f'{filenames}_encrypted.pdf', 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()

    else: 
        continue 

        #ENCRYPTED SHIT GOES HERE
#         pdfFile = open('meetingminutes.pdf', 'rb') # open the PDF you want to encrypt and name it/make it callable
# pdfReader = PyPDF2.PdfFileReader(pdfFile) # set it so a PDF file reader object
# pdfWriter = PyPDF2.PdfFileWriter() # setting up a blank/new pdf, that will be the NEW encrypted one


# # This is how you apply something to the entire PDF file, by iterating through EACH PAGE, and saying to write it/add it to the blank/new PDF created- aka the pdfWriter object
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum)) 


# # Now encrpyt/add the password you want for the file, and what you want it to be saved as
# pdfWriter.encrypt('hi') # user password = first argument, owner password = second, otherwise if just 1 argument is given, then it will be same password for both
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()