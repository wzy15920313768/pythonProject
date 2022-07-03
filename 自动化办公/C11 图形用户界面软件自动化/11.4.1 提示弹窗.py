"""
    File Name: 11.4.1 提示弹窗
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 11:10
"""

import pyautogui as gui


def alert():
    res = gui.alert(text='Are you OK?', title='OK?', button='OK')
    print(res)


def confirm():
    res = gui.confirm(text='Are you OK?', title='OK?', buttons=['OK', '很不OK'])
    print(res)


def prompt():
    res = gui.prompt(text='', title='OK?', default='写点东西吧')
    print(res)


def passwd():
    res = gui.password(text='请输入密码', title='OK?', default='', mask='*')
    print(res)


alert()
confirm()
prompt()
passwd()
