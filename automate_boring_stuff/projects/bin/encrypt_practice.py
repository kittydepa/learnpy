'''From page 302 in Automate the Boring Stuff
   Practice with encrypting PDFs'''

import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb') # open the PDF you want to encrypt and name it/make it callable
pdfReader = PyPDF2.PdfFileReader(pdfFile) # set it so a PDF file reader object
pdfWriter = PyPDF2.PdfFileWriter() # setting up a blank/new pdf, that will be the NEW encrypted one


# This is how you apply something to the entire PDF file, by iterating through EACH PAGE, and saying to write it/add it to the blank/new PDF created- aka the pdfWriter object
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum)) 


# Now encrpyt/add the password you want for the file, and what you want it to be saved as
pdfWriter.encrypt('hi') # user password = first argument, owner password = second, otherwise if just 1 argument is given, then it will be same password for both
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()