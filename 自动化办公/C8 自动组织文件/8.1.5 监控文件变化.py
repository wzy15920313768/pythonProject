"""
    File Name: 8.1.5 监控文件变化
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 16:50
"""
import time


def on_created(event):
    print(f'创建了{event.src_path}。')


def on_deleted(event):
    print(f'注意，{event.src_path}被删除了。')


def on_modified(event):
    print(f'{event.src_path}被修改。')


def on_moved(event):
    print(f'文件从{event.src_path}移动到了{event.dest_path}')


# 事件处理器
from watchdog.events import PatternMatchingEventHandler

# 要处理文件的匹配规则，*表示匹配所有文件
patterns = '*'
# 不需要处理文件的匹配规则
ignore_patterns = ''
# 是否只监听常规文件，不包含文件夹，False表示文件夹也要监听
ignore_directories = False
# 设置为True，表示区分路径大小写
case_sensitive = True
# 创建事件处理器
event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
# 绑定对应方法
event_handler.on_created=on_created
event_handler.on_deleted=on_deleted
event_handler.on_modified=on_modified
event_handler.on_moved=on_moved

# 导入观察者
from watchdog.observers import Observer

# 要监听的路径
path = 'd1'
# 是否要监听当前目录中文件发生的变化，True表示子目录的变化也监听
recursive = True
# 创建观察者
observer = Observer()
# event_handler事件处理器
observer.schedule(event_handler, path, recursive=recursive)
# 启动事件处理器
observer.start()

# 监听中断指令
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
