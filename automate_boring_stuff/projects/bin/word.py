''' From page 307 in Automate the Boring Stuff
    Reading Word Documents, initial examples  '''


import docx
doc = docx.Document('demo.docx') # make sure this existing doc is in the same cd you are in
x = len(doc.paragraphs) # to see how many 'Paragraph' objects there are in the doc
print(f'There are {x} paragraph objects in the document.')