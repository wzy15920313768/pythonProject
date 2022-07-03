"""
    File Name: 11.3.2 敲击键盘
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 10:54
"""

import pyautogui as gui


# 敲击Enter键
gui.press('enter')
gui.press('shift')


# 敲击上下左右
gui.press('up')
gui.press('down')
gui.press('left')
gui.press('right')


# 同时按住
gui.keyDown('ctrl')
gui.keyDown('w')
gui.keyUp('ctrl')
gui.keyUp('w')




