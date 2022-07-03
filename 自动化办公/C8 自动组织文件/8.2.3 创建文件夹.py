"""
    File Name: 8.2.3 创建文件夹
    Description: 通过os库或pathlib库创建文件夹
    Author: 15920313768@163.com
    Date: 2022/7/3 17:08
"""


import os
from pathlib import Path


# 递归创建目录，注意开头不能是/
os.makedirs('d1/d2/d3')

Path('d4/d5/d6').mkdir(parents=True)

