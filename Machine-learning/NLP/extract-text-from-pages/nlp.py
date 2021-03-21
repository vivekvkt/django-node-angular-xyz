#pip install PyPDF2

import PyPDF2 as pdf

file = open('/home/vivek/Desktop/Python_Test 2021.pdf','rb')

pdf_reader = pdf.PdfFileReader(file)
pdf_reader.getIsEncrypted()
pdf_reader.getNumPages()
page1 = pdf_reader.getPage(0)
#print(page1)
page2 = pdf_reader.getPage(1)
page2.extractText()

#appending write  or Merge

pdf_writer = pdf.PdfFileWriter()
pdf_writer.addPage(page2)
pdf_writer.addPage(page1)

output = open('Pages.pdf','wb')
pdf_writer.write(output)