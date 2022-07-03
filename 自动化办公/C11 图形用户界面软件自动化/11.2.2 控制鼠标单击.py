"""
    File Name: 11.2.2 控制鼠标单击
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 10:08
"""

import pyautogui as gui

# 鼠标在当前位置点击
gui.click()
# 在指定坐标点击
gui.click(x=600, y=1000)

gui.moveTo(900, 360)
# 右击
gui.click(button='right')
gui.move(-10, 10, 1)
gui.click()
# 单击滚轮
gui.click(button='middle')

# 单击多次
gui.click(clicks=2, interval=0.25)
# 双击右键
gui.click(button='right', clicks=2, interval=0.25)

# 单击不松开
gui.mouseDown()
# 松开鼠标左键
gui.mouseUp()
# 在100，100位置右击不松开
gui.mouseDown(button='right', x=100, y=100)
# 松开鼠标右键
gui.mouseUp(button='right')