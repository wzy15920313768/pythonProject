"""
    File Name: 11.3.4
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 11:00
"""


from pynput import keyboard


def on_press(key):
    try:
        print(f'{key.char}字母键被按下')
    except AttributeError:
        print(f'{key}特殊键被按下')


def on_release(key):
    print(f'{key}键被释放')
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press,
                       on_release=on_release) as listener:
    listener.join()