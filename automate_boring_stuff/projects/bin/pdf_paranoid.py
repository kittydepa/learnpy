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

Tips/help/solutions:
https://www.mkamimura.com/2016/07/python-automating-tasks-working-with.html 
https://github.com/megamillions/PDF-Paranoia/blob/master/pdfParanoia.py 

'''

## PART 1 
# a. 

import PyPDF2, os, sys

password = sys.argv[1]

for folderName, subfolder, filenames in os.walk(os.getcwd()):

    # Find each PDF after walking through the given directory
    for filename in filenames:
        if(filename.endswith('.pdf')):

            # Rewrite PDF to become encrypted
            pdfPath = os.path.join(folderName, filename)
            pdfFile = open(pdfPath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()

            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            
            resultFilename = filename[:-4] + 'encrypter.pdf'
            resultPath = os.path.join(folderName, resultFilename)
            resultPdf = open(resultPath, 'wb')

            pdfWriter.encrypt(password)
            pdfWriter.write(resultPdf)

            # Close orginal and result PDFs, to save
            pdfFile.close()
            resultPdf.close()

            # # Verfify the encryption
            # verifyReader = PyPDF2.PdfFileReader(open(resultPath, 'rb'))
            # verifyReader.decrypt(password)

            # if verifyReader.getPage(0):

            #     print('%s encrypted as %s. Deleteing %s.' %
            #                 (filename, resultFilename, filename))
                
            #     # Delete original
            #     os.unlink(pdfPath)
            
            # else:
            #     print('Encryption failed.')