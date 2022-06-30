"""
    File Name: 4.3.3 使用Pandas实现工作表中的数据排序
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/30 23:54
"""

import pandas as pd

peoples = pd.read_excel('payment.xlsx', index_col='ID')
# sort_values方法表示按值排序
peoples.sort_values(by='工资', inplace=True, ascending=False)
# 排序结果
print(peoples)

# 多列排序
peoples.sort_values(by=['靠谱', '工资'], inplace=True, ascending=[True, False])
print(peoples)

