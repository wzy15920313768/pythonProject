"""
    File Name: 4.3.4 使用pandas实现Excel数据过滤
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/1 0:01
"""

import pandas as pd

peoples = pd.read_excel('payment.xlsx', sheet_name='Sheet2', index_col='ID')
# 检查是否有NaN
'''
名称    False
分数     True
年龄    False
性别    False
dtype: bool
'''
print(peoples.isnull().any())

# 清除NaN的行
peoples.dropna(inplace=True)

print(peoples.isnull().any())

# 过滤分数大于等于60分的女性，必须要小括号
pass_womans = peoples[(peoples['性别'] == 'F') & (peoples['分数'] >= 60)]
print(pass_womans)

# 使用loc属性过滤
def score_50_to_90(score):
    return 50 <= score < 90

def age_20_to_30(age):
    return 20 <= age < 30

# 筛选条件
man = peoples[peoples['性别'] == 'M'].loc[peoples['分数'].apply(score_50_to_90)].loc[peoples['年龄'].apply(age_20_to_30)]
print(man)