"""
    File Name: 4.3.8 使用Pandas实现数据的可视化
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 12:01
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

student = pd.read_excel('merge.xlsx')

name = '名称'
score = '分数'
age = '年龄'
# sort_values方法排序，inplace表示原地修改，ascending=False，表示从大到小
student.sort_values(by=score, inplace=True, ascending=False)
# 绘制柱状图
plt.bar(student[name], student[score], color='orange')

# 设置标题
# plt.title('Student Score', fontsize=16)
# 传入字体路径，实例化对应的字体
myfont = FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf')
# 指定渲染字体
plt.title('学生分数', fontproperties=myfont, fontsize=16)
plt.title('学生分数', fontsize=16)
# 设置x轴与y轴名称
plt.xlabel(name, fontproperties=myfont)
plt.ylabel(score, fontproperties=myfont)
# x轴中要显示的名字太长，利用rotation将其旋转90°，方便显示
plt.xticks(student[name], rotation='30')
# 紧凑型布局
plt.tight_layout
plt.show()

# 重新读入，不排序
student = pd.read_excel('merge.xlsx')
name = '名称'
score = '分数'
age = '年龄'
# 指定默认字体，正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号”-“显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制折线图
student.plot(y=[score, age])
plt.title('学生分数', fontproperties=myfont, fontsize=16, fontweight='bold')
# 重新绘制x轴坐标
plt.xticks(student.index)
plt.show()

# 绘制散点图
student.plot.scatter(x=score, y=age)
plt.title('学生分数', fontsize=16, fontweight='bold')
plt.xlabel(score)
plt.ylabel(age)
plt.show()