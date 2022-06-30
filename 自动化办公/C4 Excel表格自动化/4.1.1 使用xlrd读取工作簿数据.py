"""
    File Name: 4.1.1 使用xlrd读取工作簿数据
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/25 23:51
"""

import xlrd

# 读取指定文件，r表示不转义
file = xlrd.open_workbook(r"c:\users\extraordinary\Documents\information.xls")
# 选择第一个工作表，三种写法
sheet = file.sheets()[0]
sheet = file.sheet_by_index(0)
sheet = file.sheet_by_name("Sheet1")

# 行号+列号获取单元格内容
value = sheet.cell_value(0, 0)
print(value)

# 获取工作表数目
sheets_num = file.nsheets
print("工作表数目：%s" % sheets_num)
# 工作表名称列表
sheets_names = file.sheet_names()
print("工作表名称列表：%s" % sheets_names)
# 工作表单元格行数和列数
rows, cols = sheet.nrows, sheet.ncols
print("行数：%s 列数：%s" % (rows, cols))

# 获取工作簿所有工作表
sheets = file.sheets()
for sheet in sheets:
    rows = sheet.nrows
    cols = sheet.ncols
    for row in range(rows):
        for col in range(cols):
            print(sheet.cell_value(row, col), end='\t')
        print("\n")

# 补充：数据类型的转换（日期）
# 将读入的日期数据转为元组，取0表示以1900-01-01为基准
time_tuple = xlrd.xldate_as_tuple('xxx', 0)
# 将日期数据转为datetime对象，取1表示以1904-01-01为基准
time_datetime = xlrd.xldate_as_datetime('xxx', 1)
# 将datetime格式化
time_str = time_datetime.strftime('%Y-%m-%d %H:%M:%S')