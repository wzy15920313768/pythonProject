"""
    File Name: 4.1.2 使用xlwt将数据写入工作簿
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/26 0:19
"""

import xlwt

# 创建xls类型文件对象
people = xlwt.Workbook()
# 新建工作表
sheet = people.add_sheet('extra')
# 写入数据
sheet.write(0, 0, '三生有幸')
# 重复写入报错
sheet.write(0, 0, '三生有幸')
# 保存文件
people.save(r'C:\Users\extraordinary\Documents\people.xls')