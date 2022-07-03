"""
    File Name: 8.1.2 读写文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 16:10
"""

f = open(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', encoding='utf-8')
# f.read()读取整个文件，占资源较多
print(f.read())
f.close()

# 逐行读取，耗用资源少
f = open(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', encoding='utf-8')
for line in f.readlines():
    print(line)
f.close()

# 通过只读方式打开文件无法添加新内容，若只读文件句柄没有关闭，通过open()只写方式打开会出现问题
# fr = open(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', encoding='utf-8')
# fw = open(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', encoding='utf-8')
# fw.write('新内容')
# print('读取：', fr.read())
# fr.close()
# fw.close()

print("============ 使用 with open 方法 ============")
# 使用关键字，文件使用完后会被自动关闭
with open(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', encoding='utf-8') as f:
    print(f.read())


# 模拟open()方法
class myopen():
    '''
    模拟使用with关键字的open方法
    '''
    def __init__(self, filepath, mode, encoding):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding


    def __enter__(self):
        print('打开文件')
        self.f = open(self.filepath, self.mode, encoding=self.encoding)
        return self.f


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('关闭文件')
        self.f.close()


print("============ 模拟open()方法 ============")
with myopen(r'C:\Users\extraordinary\Documents\todolist.txt', 'r', 'utf-8') as f:
    res = f.read()
    print(res)

# 这种写模式会覆盖原本内容
with open('测试.txt', 'w', encoding='utf-8') as f:
    f.write('python自动化任务，cool~ wzy')

# 追加模式
with open('测试.txt', 'a', encoding='utf-8') as f:
    f.write('\npython自动化任务，good~ wzy')


# 以二进制形式读写
with open('测试.txt', 'wb') as f:
    f.write('新添加的内容'.encode('utf-8'))
    f.write('新添加的内容'.encode('utf-8'))

with open('测试.txt', 'rb') as f:
    # 读取二进制
    print(f.read())


# 文件不存在则执行，否则抛出异常
with open('测试1.txt', 'x') as f:
    f.write('新添加的内容')