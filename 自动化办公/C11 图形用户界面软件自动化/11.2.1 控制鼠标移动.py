"""
    File Name: 11.2.1 控制鼠标移动
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 9:59
"""

import pyautogui

# 瞬间移动
pyautogui.moveTo(100, 100)
# 匀速移动
pyautogui.moveTo(500, 500, 2)

pyautogui.PAUSE = 1

# 相对移动
pyautogui.move(-100, -100, 1)