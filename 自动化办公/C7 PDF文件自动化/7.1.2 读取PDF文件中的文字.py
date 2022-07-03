"""
    File Name: 7.1.2 读取PDF文件中的文字
    Description: getText()方法提取文字
    Author: 15920313768@163.com
    Date: 2022/7/2 14:44
"""

import fitz
from pathlib import Path

pdfpath = Path(r'C:\Users\extraordinary\Downloads\Java开发工程师_吴赠禹.pdf')

def extract_all_document_text():
    '''
    提取PDF中所有的文字
    缺点：提取的文字无序
    :return:
    '''
    pdf = fitz.open(pdfpath)
    content = ''
    for page in pdf:
        text = page.get_text()
        content += text
    with open('保存提取的文字.txt', 'w') as f:
        f.write(content)

def extract_all_document_text_by_block():
    '''
    提取PDF中的所有文字
    通过块读取的方式，实现顺序读取
    block中有很多信息可以用于排序，从而获取正确的顺序
    :return:
    '''
    pdf = fitz.open(pdfpath)
    content = []
    for page in pdf:
        # 获取文本块
        blocks = page.get_text('blocks')
        content.extend(blocks)
    with open('保存提取的文字_有序.txt', 'w') as f:
        content = '\n'.join([_[4] for _ in content])
        f.write(content)

extract_all_document_text()
extract_all_document_text_by_block()