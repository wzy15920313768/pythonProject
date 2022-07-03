"""
    File Name: 11.2 控制鼠标
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 9:57
"""

# 屏幕大小
import pyautogui

screen_size = pyautogui.size()
print(screen_size)

# 获取鼠标指针当前位置
while True:
    mouse_position = pyautogui.position()
    print(mouse_position)
