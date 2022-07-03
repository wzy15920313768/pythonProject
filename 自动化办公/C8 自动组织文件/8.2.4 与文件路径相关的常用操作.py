"""
    File Name: 8.2.4 与文件路径相关的常用操作
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 17:13
"""


from pathlib import Path


txtpath = Path(r'C:\Users\extraordinary\PycharmProjects\pythonProject\自动化办公\C8 自动组织文件\8.1.1 获取文件属性.py')
# 文件是否存在
print(txtpath.exists())

# 获取当前路径
pwd = Path.cwd()
print(pwd)

# 相对与当前路径
path = pwd.joinpath('..', 'code')
print(path)

# 通过Path.is_dir()判断是否为文件夹
print(txtpath.is_dir())
print(txtpath.is_file())

# 通过Path.samefile判断两个文件是否相同，要求文件存在（文件名相同，复制的文件为什么不相同？）
target1 = Path(r'C:\Users\extraordinary\PycharmProjects\pythonProject\自动化办公\C8 自动组织文件\8.1.1 获取文件属性.py')
target2 = Path(r'C:\Users\extraordinary\PycharmProjects\pythonProject\自动化办公\C8 自动组织文件\d1\8.1.1 获取文件属性.py')
print(Path.samefile(target1, target2))


# 通过Path对象获取文件名、属性名、扩展名、所在目录
print(f'文件名：{txtpath.name}')
print(f'扩展名：{txtpath.suffix}')
print(f'所在目录：{txtpath.parent}')


# 处理文件夹中的所有文件
def find_all_py(dir):
    # 递归遍历dir文件夹，找到*.py文件
    for p in dir.rglob('*.py'):
        # 深度
        depth = len(p.relative_to(dir).parts)
        print(p.name, depth)


find_all_py(Path.cwd())


# 通过iterdir方法获取当前文件夹下所有文件，可以计算出当前目录中不同类型文件的个数
from collections import Counter


gen = []
# 遍历当前文件夹中的文件
for i in Path.cwd().iterdir():
    # 将文件类型添加到list中
    gen.append(i.suffix)

# 计算重复内容的个数
print(Counter(gen))