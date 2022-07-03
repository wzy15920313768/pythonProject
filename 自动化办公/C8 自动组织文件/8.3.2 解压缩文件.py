"""
    File Name: 8.3.2 解压缩文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 17:31
"""
import tarfile
import zipfile
from pathlib import Path


# 解压的目标路径
# target_path = Path.cwd()
# zippath = Path('new.zip')
# # 创建ZipFile对象
# zip_file = zipfile.ZipFile(zippath)
# # 解压
# zip_file.extractall(target_path)
# zip_file.close()
# print('done!')
#
# # 解压.tar.gz格式
# path = 'new.tar.gz'
# target_path = '.'
# tar = tarfile.open(path, 'r:gz')
# # 获取压缩文件中所有文件的名称
# file_names = tar.getnames()
# print(f'tar zip files name: {file_names}')
#
# # 解压
# tar.extractall(target_path)
# print('done!')

# 解压部分文件
target_path = Path.cwd()
zippath = Path('new.zip')
# 创建ZipFile对象
zip_file = zipfile.ZipFile(zippath)
# 需要被解压的文件
need_unzip = ['8.1.1 获取文件属性.py']
# 返回zip文件中包含所有文件和文件夹列表
names = zip_file.namelist()
print(names)
for fn in names:
    # 判断是否是解压文件
    files = [f for f in need_unzip if f in fn]
    if files:
        print(fn)
        # 解压该文件
        zip_file.extract(fn, target_path)


zip_file.close()
print('done!')