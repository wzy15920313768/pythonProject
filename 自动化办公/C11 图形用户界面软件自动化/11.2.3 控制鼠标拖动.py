"""
    File Name: 11.2.3 控制鼠标拖动
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 10:17
"""

import pyautogui as gui

# 按住鼠标左键，在2s内拖动到屏幕（x, y）位置
gui.dragTo(100, 0, duration=2, button='left')

# 相对拖动
gui.moveTo(660, 1000)
gui.drag(500, 0, duration=1, button='left')