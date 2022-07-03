"""
    File Name: 8.1.3 重命名文件
    Description: 扩展：通过程序扩展名通配
    Author: 15920313768@163.com
    Date: 2022/7/3 16:38
"""

from pathlib import Path


txtpath = Path(r'测试.txt')
txtpath.rename(txtpath.parent.joinpath('测试x.txt'))