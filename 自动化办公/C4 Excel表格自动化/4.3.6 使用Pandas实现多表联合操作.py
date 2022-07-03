"""
    File Name: 4.3.6 使用Pandas实现多表联合操作
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 10:48
"""

import pandas as pd

# 学生姓名表（以下三张表皆为存在相同名称列的情况）
student = pd.read_excel('student.xlsx', sheet_name='name')
# 分数表
score = pd.read_excel('score.xlsx', sheet_name='score')
# 年龄表
age = pd.read_excel('age.xlsx', sheet_name='age')

# 合并，fillna方法将NaN填充为0，不指定left则取交集合并，on指定合并列（关联条件）
table = student.merge(score, how='left', on='ID').fillna(0)
# 将分数列中的数据设置为整型
table['分数'] = table['分数'].astype(int)

table2 = table.merge(age, how='left', on='ID').fillna(0)
table2['年龄'] = table2['年龄'].astype(int)

print(table2)
# 指定索引列
table2.set_index('ID', inplace=True)
table2.to_excel('merge.xlsx')

print("==========")

# 过滤条件
pass_womans = table2[(table2['年龄'] >= 20) & (table2['分数'] >= 60)]
print(pass_womans['名称'])