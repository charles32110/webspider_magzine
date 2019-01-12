#coding:utf-8
from reportlab.pdfgen import canvas
import os
import time
#http://img-qn.bookan.com.cn/jpage3/639/639-451428/4f22c2c7_big.jpg,
"""
x = 'tets'
def hello(c):
    c.drawString(100, 100, "Hello World")
    


c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()

c = canvas.Canvas('%s.pdf'%x, pagesize=portrait(A4))
"""

#c = canvas.Canvas(os.path.basename('pict')+".pdf")
#c = canvas.Canvas('heloo333.pdf')
#c.drawImage('/Users/zhangguanqin/PycharmProjects/tets/pict/1.jpg', 0, 0, w, h)
#c.save()

def convert_images_to_pdf():
    pages = 0
    (w, h) = (600, 840)
    c = canvas.Canvas('/Users/zhangguanqin/PycharmProjects/tets/%s'%time.asctime()+'.pdf')
    l = os.listdir('/Users/zhangguanqin/PycharmProjects/tets/pict')
    l.sort(key= lambda x:int(x[:-4]))
    for i in l:
        f = '/Users/zhangguanqin/PycharmProjects/tets/pict' + os.sep + str(i)
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()
convert_images_to_pdf()
