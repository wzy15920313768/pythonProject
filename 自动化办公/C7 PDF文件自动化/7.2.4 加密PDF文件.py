"""
    File Name: 7.2.4 加密PDF文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 22:33
"""

import PyPDF4

pdfReader = PyPDF4.PdfFileReader(r'C:\Users\extraordinary\Documents\image.pdf')
pdfWriter = PyPDF4.PdfFileWriter()
# 将内容读取并添加到pdfWriter中
for pagenum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pagenum))
# 设置密码
pdfWriter.encrypt('123456')
with open('encrypt.pdf', 'wb') as f:
    pdfWriter.write(f)