''' 
Project from pg. 316 in Automate the Boring Stuff

-------------------------------------------------------------------------

PART 1

Using os.walk(), write a script that will:
a. go through every PDF in a folder & its subfolders
b. encrypt each of the PDFs using a pw given in teh command line
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

