## Copying PDF pages using PyPDF2 (from ch 13, pg. 299)


import PyPDF2


# First open the PDF files within Python
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

# Next, set the PDF files to a PdfFileReader object
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Create an empty PdfFileWriter object, where the new/blank PDF file will be
pdfWriter = PyPDF2.PdfFileWriter()


# Copying the pages from both of the PDF files
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum) # Get the page object with getPage()
    pdfWriter.addPage(pageObj) # Pass the Page object into PdfFileWriter's addPage()
                               # This adds the pages from pdf1 to our new pdfWriter object/PDF file

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)



# Write a new PDF called 'combinedminutes', by using the write() method
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close() # Close them to save

pdf1File.close()
pdf2File.close()