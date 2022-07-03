"""
    File Name: 4.3.7 使用Pandas对Excel数据进行统计运算
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 11:40
"""

import pandas as pd

peoples = pd.read_excel('table.xlsx', index_col='ID')

column_names = ['小测1', '小测2', '小测3']

# 对每一行中的每一列进行求和操作
row_sum = peoples[column_names].sum(axis=1)
# 对每一行中的每一列进行求平均操作
row_mean = peoples[column_names].mean(axis=1)

total = '总分'
average = '平均分'
peoples[total] = row_sum
peoples[average] = row_mean
column_names += [total, average]

# axis默认值为0，对每一列中的每一行进行求平均操作
col_mean = peoples[column_names].mean()
# print(col_mean)
col_mean['名称'] = 'Summary'
# append方法添加新的一行，ignore_index为True表示忽略index
peoples = peoples.append(col_mean, ignore_index=True)

print(peoples)