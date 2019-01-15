#coding:utf-8
import os
import PIL
import time
from reportlab.pdfgen import canvas

def savepdf():
    pages = 0
    a = time.asctime()
    c = canvas.Canvas('/Users/zhangguanqin/PycharmProjects/tets/%s'%a + '.pdf')
    (w, h) = (600, 840)

    path = "/Users/zhangguanqin/PycharmProjects/tets/pict"  # 待读取的文件夹
    path_list = os.listdir(path)
    path_list.sort()
    path_list.sort(key=lambda x:int(x[:-4]))# 对读取的路径进行排序
    for ff in path_list:
        f = '/Users/zhangguanqin/PycharmProjects/tets/pict/' + ff
        c.drawImage(f,0,0,w,h)
        c.showPage()
        pages = pages + 1
    c.save()
savepdf()