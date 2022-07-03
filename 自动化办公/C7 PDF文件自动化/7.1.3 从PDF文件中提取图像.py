"""
    File Name: 7.1.3 从PDF文件中提取图像
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 15:23
"""

import fitz
from pathlib import Path

imgdir = Path("images")

# 文件夹不存在，则需创建
if not imgdir.is_dir():
    imgdir.mkdir(parents=True)

def get_all_images(pdfpath):
    '''
    获取PDF中所有的图片
    :param pdfpath:
    :return:
    '''
    pdf = fitz.open(pdfpath)
    print(pdf)
    print(type(pdf))
    xreflist = []
    for page_num in range(len(pdf)):
        print(page_num)
        # 获取某页所有的图片数据
        imgs = pdf.get_page_images(page_num)
        print(imgs)
        print("=== imga ===")
        for img in imgs:
            print("=== img ===")
            xref = img[0]
            if xref in xreflist:
                # 已处理过，不再处理
                continue
            # 获取图片信息
            pix = recoverpix(pdf, img)
            # 获取原始图像
            if isinstance(pix, dict):
                # 图像扩展名：png、jpg等
                ext = pix['ext']
                # 图像原始数据
                imgdata = pix['image']
                # 图像颜色通道
                n = pix['colorspace']
                # 图像保存路径
                imgfile = imgdir.joinpath(f"img-{xref}.{ext}")
            # 获取像素图
            else:
                # 图像保存路径
                imgfile = imgdir.joinpath(f"img-{xref}.png")
                n = pix.n
                imgdata = pix.tobytes()
            if len(imgdata) <= 2048:
                # 图像大小至少大于或等于2KB，否则就忽略
                continue
            # 保存图像
            with open(imgfile, 'wb') as f:
                f.write(imgdata)
            # 不再重复处理相同的xref
            xreflist.append(xref)
            print(f'{imgfile} save')


def getimage(pix):
    # 像素图色彩空间不为4，表示没有透明层
    if pix.colorspace.n != 4:
        return pix
    return fitz.Pixmap(fitz.csRGB, pix)


def recoverpix(pdf, item):
    '''
    恢复图片——处理不同类型的图像，处理遮罩层
    :param pdf:
    :param item:
    :return:
    '''
    xref = item[0]
    # xref对应图像的遮罩层
    smask = item[0]
    if smask == 0:
        # 没有遮罩层，直接导出图像
        return pdf.extractImage(xref)
    pix1 = fitz.Pixmap(pdf, xref)
    pix2 = fitz.Pixmap(pdf, smask)
    # 完整性判断
    if not all([
        # 像素图矩形相同
        pix1.irect == pix2.irect,
        # 像素图都没有Alpha层
        pix1.alpha == pix2.alpha == 0,
        # pix2像素图每像素只有一维
        pix2.n == 1
    ]):
        pix2 = None
        return getimage(pix1)

    # 复制pix1，用于添加Alpha通道
    pix = fitz.Pixmap(pix1)
    pix.set_alpha(pix2.samples)
    pix1 = pix2 = None
    return getimage(pix)


def main():
    pdfpath = Path(r'C:\Users\extraordinary\Documents\image.pdf')
    get_all_images(pdfpath)

if __name__ == '__main__':
    main()
