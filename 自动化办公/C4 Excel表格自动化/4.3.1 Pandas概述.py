"""
    File Name: 4.3.1 Pandas概述
    Description:
    Author: 15920313768@163.com
    Date: 2022/6/28 13:26
"""

import pandas as pd

# 实例化Series对象
s1 = pd.Series([1,2,3], index=[1,2,3], name='s1')
# 输出s1
print(s1)
# 输出Series对象的索引
print(s1.index)
# 输出Series对象中索引为1的值
print(s1[1])

# 创建DataFrame对象
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
# 使用Series对象实例化DataFrame对象
df = pd.DataFrame([s1, s2, s3])
# Series对应DataFrame的每一行
print(df)

# 通过字典构建DataFrame对象，每一列由Series构成
df2 = pd.DataFrame({
    s1.name: s1,
    s2.name: s2,
    s3.name: s3
})
print("===")
print(df2)

df2.sort_values(by='C', ascending=False, inplace=True)
print(df2)
