"""
    File Name: 8.1.4 删除文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 16:44
"""


from pathlib import Path


# txtpath = Path('测试x.txt')
# # unlink() 删除文件，不回收
# txtpath.unlink()
#
# dir = Path('empty')
# # 删除空目录
# dir.rmdir()

txtpath = Path(r'C:\Users\extraordinary\Documents\todolist - 副本.txt')

# 垃圾桶文件夹路径
trashpath = Path(r'C:\Users\extraordinary\Documents\trash')

# 将文件移动到垃圾桶，完成删除
txtpath.rename(trashpath.joinpath(txtpath.name))