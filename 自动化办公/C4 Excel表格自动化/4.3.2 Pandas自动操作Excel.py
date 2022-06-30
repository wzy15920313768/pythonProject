"""
    File Name: 4.3.2 Pandas自动操作Excel
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/28 13:34
"""

import pandas as pd

filepath = 'test.xlsx'
# 读出工作簿中名为Sheet的工作表
people = pd.read_excel(filepath, sheet_name='Sheet')

# header=2表示从第3行开始，相当于跳过了前2行（pandas会自动跳过空行）
people1 = pd.read_excel(filepath, header=2, sheet_name='Sheet')

# skiprows跳过开头几行，usecols表示使用哪些列的数据
people13 = pd.read_excel(filepath, sheet_name='Sheet', skiprows=4, usecols='E:H')

# 指定id列为索引，dtype设置某一列数据的类型
people2 = pd.read_excel(filepath, sheet_name='Sheet1', index_col='id', dtype={'name': str, 'age': str})

# 通过字典形式构建DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['张三', '李四', '王五'],
    'age': [28, 25, 30]
})
# 自定义索引
df = df.set_index('id')
df.to_excel('people.xlsx')

# 利用pandas整理excel
import warnings
warnings.filterwarnings("ignore")
# 读入工作簿，一共有10行
people = pd.read_excel('peoplex.xlsx', skiprows=4, usecols='B:E', dtype={'ID': str, 'gender': str, 'birthday': str})
print("index: %s", people.index)
# 将工作表读取成DataFrame对象
from datetime import date, timedelta

# 开始日期
startday = date(2022, 6, 29)
for i in people.index:
    # 累加ID
    people.at[i, 'ID'] = i + 1
    # 判断性别
    people.at[i, 'gender'] = 'Male' if i % 2 == 0 else 'Female'
    # 计算生日时间
    people.at[i, 'birthday'] = date(startday.year + i, startday.month, startday.day)

# inplace表示就地修改DataFrame，不必再重新创建一个新的DataFrame来存储修改后的状态
people.set_index('ID', inplace=True)
people.to_excel('people2.xlsx')

# 向指定列加钱
peoples = pd.read_excel('people3.xlsx', index_col='ID')
'''
加钱
'''
def add_money(x):
    return x + 1000


# series对象加1000
peoples['money'] = peoples['money'] + 1000
# apply逐个元素调用
peoples['money'] = peoples['money'].apply(add_money)
# apply会逐个元素地调用匿名函数
peoples['money'] = peoples['money'].apply(lambda x : x + 1000)
peoples.to_excel('people4.xlsx')