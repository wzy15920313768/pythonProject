"""
    File Name: 4.1.3 使用xlutils修改工作簿数据
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/26 9:57
"""

import xlrd
from xlutils.copy import copy

# 读入数据，获取Book对象，formatting_info=True表示复制样式
rd_book = xlrd.open_workbook(r'C:\Users\extraordinary\Documents\information.xls', formatting_info=True)
# 获取第一个工作表
rd_sheet = rd_book.sheets()[0]
# 复制为可写入对象
wt_book = copy(rd_book)
# 从可写入对象获取Sheet对象
wt_sheet = wt_book.get_sheet(0)
# 循环处理每一行第一列数据，修改其中的内容
for row in range(rd_sheet.nrows):
    wt_sheet.write(row, 0, '修改内容')
wt_book.save(r'C:\Users\extraordinary\Documents\informationX.xls')

