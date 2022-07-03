"""
    File Name: 8.1.1 获取文件属性
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 16:02
"""

import time
from pathlib import Path


def get_filesize(filepath):
    # 获取文件大小，单位为B
    fsize = Path(filepath).stat().st_size
    # 转换为MB
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 4)


fsize = get_filesize(r'C:\Users\extraordinary\Downloads\WeChatSetup.exe')
print(f'文件大小：{fsize}MB')


def get_time(timestamp):
    '''
    格式化时间戳
    :param timestamp:
    :return:
    '''
    t = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', t)


filepath = r'C:\Users\extraordinary\Downloads\WeChatSetup.exe'
# 文件创建时间
ctime = Path(filepath).stat().st_ctime
ctime = get_time(ctime)
# 文件修改时间
mtime = Path(filepath).stat().st_mtime
mtime = get_time(mtime)
print(f'创建时间：{ctime}\n修改时间：{mtime}')
