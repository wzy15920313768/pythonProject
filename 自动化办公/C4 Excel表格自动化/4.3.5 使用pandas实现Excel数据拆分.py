"""
    File Name: 4.3.5 使用pandas实现Excel数据拆分
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/1 0:11
"""

import pandas as pd

peoples = pd.read_excel('payment.xlsx', sheet_name='Sheet2', index_col='ID')

# 拆分姓名
df = peoples['名称'].str.split(expand=True)
# 创建列
peoples['姓氏'] = df[0]
# 创建列
peoples['名字'] = df[1]
print(peoples)