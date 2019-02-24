from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import gray
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("Vera", "Vera.ttf"))
pdfmetrics.registerFont(TTFont("VeraBd", "VeraBd.ttf"))
pdfmetrics.registerFont(TTFont("VeraIt", "VeraIt.ttf"))
pdfmetrics.registerFont(TTFont("VeraBI", "VeraBI.ttf"))

c = canvas.Canvas(filename = "potwierdzenie.pdf", pagesize = A4)
width, height = A4
font_size = 9

def nadawca():
    dane_nadawcy = []
    with open("nadawca.txt", 'r') as nadawca_txt:
        for line in nadawca_txt:
            dane_nadawcy.append(line.rstrip())
    pos_x = 15
    pos_y = height - 59
    for line in dane_nadawcy:
        c.setFont("Vera", font_size)
        c.drawString(pos_x, pos_y, line)
        pos_y -= font_size + 1

def odbiorca():
    dane_odbiorcy = []
    with open("odbiorca.txt", 'r') as odbiorca_txt:
        for line in odbiorca_txt:
            dane_odbiorcy.append(line.rstrip())
    pos_x = 15
    pos_y = height - 139
    for line in dane_odbiorcy:
        c.setFont("Vera", font_size)
        c.drawString(pos_x, pos_y, line)
        pos_y -= font_size + 1

def geometria():
    rect_width = width / 2.0 - 13
    rect2_width = rect_width - 137
    rect_height = 70 * mm
    rect2_height = 20 * mm
    rect_x = 13
    rect2_x = 150
    rect_y = height - 13 - rect_height
    rect2_y = rect_y + 50 * mm
    pos_y = height - 38
    posc_y = height - 173
    c.setDash(1,2)
    c.setStrokeColor(gray)
    c.rect(rect_x, rect_y, rect_width, rect_height, stroke = 1, fill = 0)
    c.line(rect2_x, rect2_y, rect2_x, height - 13)
    c.line(rect2_x, rect2_y, width / 2.0, rect2_y)
    c.line(rect_x, pos_y, rect2_x, pos_y)
    c.line(200 - 4, rect_y, 200 - 4, rect2_y)
    c.circle(247, posc_y, 25, stroke=1, fill=0)


def tekst():
    pos_x = 15
    pos_y = height - 23
    tekst = []
    pos2_x = 200
    pos2_y = height - 86
    with open("tekst.txt", 'r') as tekst_txt:
        for line in tekst_txt:
            tekst.append(line.rstrip())
    c.setFont("VeraBd", font_size)
    c.drawString(pos_x, pos_y, tekst[0])
    c.setFont("Vera", font_size)
    c.drawString(pos_x, pos_y - 10, tekst[1])
    c.setFont("VeraBd", font_size)
    c.drawString(pos_x, pos_y - 26, tekst[2])
    c.setFont("VeraBd", font_size)
    c.drawString(pos_x, pos_y - 106, tekst[3])
    c.setFont("VeraBd", font_size)
    c.drawString(pos2_x, pos2_y, tekst[4])
    c.setFont("Vera", font_size)
    c.drawString(pos2_x, pos2_y - 11, tekst[5])
    c.setFont("Vera", font_size)
    c.drawString(pos2_x, pos2_y - 22, tekst[6])
    c.setFont("Vera", font_size)
    c.drawString(pos2_x, pos2_y - 33, tekst[7])
    c.setFont("Vera", font_size)
    c.drawString(pos2_x, pos2_y - 44, tekst[8])

nadawca()
odbiorca()
geometria()
tekst()

c.save()
