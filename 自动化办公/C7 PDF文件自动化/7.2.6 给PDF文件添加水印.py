"""
    File Name: 7.2.6 给PDF文件添加水印
    Description: 本质是将水印文件合并到PDF文件，可通过reportlab生成水印文件。
    Author: 15920313768@163.com
    Date: 2022/7/2 22:40
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def create_watermark(content):
    '''
    创建水印
    :param content:
    :return:
    '''
    file_name = "watermark.pdf"
    # 创建水印画布
    c = canvas.Canvas(file_name, pagesize=(30*cm, 30*cm))
    # 移动坐标原点（坐标系左下为（0，0））
    c.translate(10*cm, 2*cm)
    # 设置字体
    c.setFont("Helvetica", 80)
    # 指定描边的颜色
    c.setStrokeColorRGB(0, 1, 0)
    # 指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    # 旋转45°，坐标系被旋转
    c.rotate(45)
    # 指定填充颜色
    c.setFillColorRGB(0.6, 0, 0)
    # 设置透明度，1为不透明
    c.setFillAlpha(0.2)
    # 绘制文本
    c.drawString(3*cm, 0*cm, content)
    # 设置透明度
    c.setFillAlpha(0.4)
    # 关闭并保存PDF文件
    c.save()
    return file_name


from pathlib import Path
from PyPDF4 import PdfFileReader, PdfFileWriter


def add_watermark(input_pdf, output):
    '''
    添加水印
    :param input_pdf:
    :param output:
    :return:
    '''
    watermark = Path('watermark.pdf')
    # 不存在则创建
    if not watermark.is_file():
        create_watermark("python")
    watermark_obj = PdfFileReader(str(watermark))
    watermark_page = watermark_obj.getPage(0)
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    # 给所有页面添加水印
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
    with open(output, 'wb') as out:
        pdf_writer.write(out)


add_watermark(r'C:\Users\extraordinary\Documents\table.pdf', 'table_watermark.pdf')

