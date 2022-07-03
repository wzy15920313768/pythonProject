"""
    File Name: 8.3.3 破解加密压缩文件
    Description: 鸡肋案例
    Author: 15920313768@163.com
    Date: 2022/7/3 17:38
"""

import zipfile

zippth = 'new.zip'
pwd_path = 'passwd.txt'
targetpath = '.'
zip = zipfile.ZipFile(zippth)


def unzip(pwd):
    try:
        # 解压，pwd为解压时使用的密码
        zip.extractall(path=targetpath, pwd=pwd.encode('utf-8'))
        print(f'密码为：{pwd}')
        return True
    except:
        return False


with open(pwd_path, 'r') as f:
    for pwd in f.readlines():
        pwd = pwd.strip()
        if unzip(pwd):
            break

