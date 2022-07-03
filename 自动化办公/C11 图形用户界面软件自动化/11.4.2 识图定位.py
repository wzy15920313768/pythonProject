"""
    File Name: 11.4.2 识图定位
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 11:28
"""


import pyautogui as gui
import time


time.sleep(2)

# 设置自动化时间操作间隔
gui.PAUSE = 0.1
print('show time')


def delete_chat_info():
    '''
    删除聊天信息
    :return:
    '''
    # 屏幕截图
    gui.screenshot()
    # 定位聊天气泡图
    chat_bubble = gui.locateCenterOnScreen(r'C:\Users\extraordinary\Pictures\Saved Pictures\WeChat\0.png')
    if not chat_bubble:
        print('定位聊天气泡图失败')
        return
    # 聊天气泡图右移120像素则是联系人的坐标位置
    x = chat_bubble[0] + 120
    y = chat_bubble[1]
    # 右击，让微信弹出删除列表框
    gui.rightClick(x, y)
    gui.screenshot()
    # 定位删除按钮
    delete_button = gui.locateCenterOnScreen(r'C:\Users\extraordinary\Pictures\Saved Pictures\WeChat\1.png')
    if not delete_button:
        print('定位删除按钮失败')
        return
    # 模拟鼠标单击删除按钮
    gui.click(delete_button)


def main():
    for i in range(100):
        delete_chat_info()


if __name__ == '__main__':
    main()