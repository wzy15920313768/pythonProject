"""
    File Name: 补充：DOCX转PDF
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 15:57
"""

from docx2pdf import convert

input = r"C:\Users\extraordinary\Documents\table.docx"
output = r"C:\Users\extraordinary\Documents\table.pdf"
# 以下两行可省略
# file = open(output, 'w')
# file.close()
convert(input, output)