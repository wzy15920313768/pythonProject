"""
    File Name: 7.1.4 从PDF文件中提取表格
    Description: pdfplumber、camelot可以提取具有标准样式的表格，以及部分无边界但文字对齐的表格。
    Author: 15920313768@163.com
    Date: 2022/7/2 21:51
"""

from pathlib import Path
import pdfplumber
import pandas as pd


def use_pdfplumber(pdfpath):
    pdf = pdfplumber.open(pdfpath)
    # 获取具有表格的某页PDF
    p0 = pdf.pages[0]
    # 获取PDF中的表格
    try:
        table = p0.extract_table()
        df = pd.DataFrame(table[1:], columns=table[0])
        df.to_csv('table.csv')
    except Exception as e:
        print('无法解析PDF中的表格')
        raise e


pdfpath = Path(r'C:\Users\extraordinary\Documents\table.pdf')
use_pdfplumber(pdfpath)


import camelot

def use_camelot(pdfpath):
    tables = camelot.read_pdf(str(pdfpath))
    # 开启压缩包模式，可选
    tables.export('table2.csv', f='csv', compress=True)


use_camelot(pdfpath)

