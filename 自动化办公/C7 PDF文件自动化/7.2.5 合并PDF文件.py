"""
    File Name: 7.2.5 合并PDF文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 22:37
"""

import PyPDF4

# 要和并的PDF对象
pdfReaders = [PyPDF4.PdfFileReader(r'C:\Users\extraordinary\Documents\image.pdf'),
              PyPDF4.PdfFileReader(r'C:\Users\extraordinary\Documents\image.pdf')]
pdfWriter = PyPDF4.PdfFileWriter()
for reader in pdfReaders:
    for pageNum in range(reader.numPages):
        page = reader.getPage(pageNum)
        pdfWriter.addPage(page)

# 持久化
with open('合并.pdf', 'wb') as f:
    pdfWriter.write(f)
