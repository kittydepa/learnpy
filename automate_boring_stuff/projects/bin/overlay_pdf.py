# Adding an overlay to multiple pages of a PDF

import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader