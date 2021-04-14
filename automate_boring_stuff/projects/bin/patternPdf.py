## Combining 2 PDFs of the same cross stitch pattern

import PyPDF2

# First open the existing PDF files 
pattern1 = open('green-all.pdf', 'rb')
pattern2 = open('green_easy.pdf', 'rb')

# Next, set the PDF files to a PdfFileReader object
pdf1 = PyPDF2.PdfFileReader(pattern1)
pdf2 = PyPDF2.PdfFileReader(pattern2)

# Create an empty PdfFileWriter object/a blank PDF file
pdfWriter = PyPDF2.PdfFileWriter()


# Copy the pages from each PDF file
for pageNum in range(pdf1.numPages):
    pages = pdf1.getPage(pageNum)
    pdfWriter.addPage(pages)

for pageNum in range(pdf2.numPages):
    pages = pdf2.getPage(pageNum)
    pdfWriter.addPage(pages)


pdfOutputFile = open('combined_pattern.pdf', 'wb') # wb = write binary. PDF files are binary
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pattern1.close()
pattern2.close()