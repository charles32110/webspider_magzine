from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape

x = 'tets'
def hello(c):
    c.drawString(100, 100, "Hello World")


c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()

c = canvas.Canvas('%s.pdf'%x, pagesize=portrait(A4))