"""
    File Name: 11.2.5 监控鼠标操作
    Description: pynput监控鼠标
    Author: 15920313768@163.com
    Date: 2022/7/3 10:44
"""

from pynput import mouse


def on_move(x, y):
    print(f'鼠标移动到（{x}, {y}）位置')


def on_click(x, y, button, pressed):
    if pressed:
        status = '按下'
    else:
        status = '松开'
    print(f'{status}鼠标的位置在（{x}, {y}）')

    # 松开鼠标结束程序
    if not pressed:
        return False


def on_scroll(x, y, dx, dy):
    if dy < 0:
        status = '下'
    else:
        status = '上'
    print(f'向{status}滚动到（{x}, {y}）')


with mouse.Listener(on_move=on_move,
                    on_click=on_click,
                    on_scroll=on_scroll) as listener:
    listener.join()