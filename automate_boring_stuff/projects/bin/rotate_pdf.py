## Rotating 1 page of PDF, and saving it as it's own PDF

import PyPDF2

# First open the PDF, and save it as a PdfFileReader object
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

# Indicate which page you would like to have rotated, save it as an object, and how
page = pdfReader.getPage(0)  # setting the page number to an object
page.rotateClockwise(90) # rotate 90 degrees

# Create a new/blank PDF, then add the page you rotated above to it
pdfWriter = PyPDF2.PdfFileWriter() 
pdfWriter.addPage(page)


# Create an object and name for the new pdf
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile) 

resultPdfFile.close()
minutesFile.close()