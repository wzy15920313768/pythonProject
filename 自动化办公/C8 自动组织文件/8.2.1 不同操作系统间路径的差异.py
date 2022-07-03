"""
    File Name: 8.2.1 不同操作系统间路径的差异
    Description: 不同系统路径存在差异，使用内置pathlib库
    Author: 15920313768@163.com
    Date: 2022/7/3 17:02
"""

from pathlib import Path


# 硬编码不具备跨平台（Windows反斜杠，macOS正斜杠）
path = 'Users/extraordinary/Desktop'
print(f'硬编码的路径：{path}')

path2 = Path().joinpath('Users', 'extraordinary', 'Desktop')
print(f'软编码的路径：{path}')

