import readDoc1

print(readDoc1.getText('demo.docx')) 

'''
Run this program in the terminal. The output is the plain text from the 'demo.docx')

- Note that the function getText() created/first defined in readDoc1.py.
  What getText() does is allow you to extract text from a docx file, and append it to a list so you can print it in Python
  
  What we are doing here in this program is:
  1) Importing readDoc1 because that is where the getText() function is, and we want to apply i here.
  2) We use print, and apply our getText() function to the Word doc we want to extract text from; in this case demo.docx 
'''