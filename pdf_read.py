import PyPDF2
import nltk
import re
pdf_file = open('/Users/alex/Desktop/二手车交易的案例.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

pdf_file.close()
# print(text)


