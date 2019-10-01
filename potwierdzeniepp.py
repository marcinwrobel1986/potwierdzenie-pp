from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import gray
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class ConfGenerator:
    def __init__(self, kind='P. PRIORYTETOWA'):
        self.kind = kind
        self.filename = 'post_confirmation.pdf'
        self.sender_filename = 'sender.txt'
        self.recipient_filename = 'recipient.txt'

        self.font_vera = pdfmetrics.registerFont(TTFont("Vera", "Vera.ttf"))
        self.font_vera_bd = pdfmetrics.registerFont(TTFont("VeraBd", "VeraBd.ttf"))
        self.canvas = canvas.Canvas(filename=self.filename, pagesize=A4)
        self.font_size = 9

        self.sender_data = None
        self.recipient_data = None

        self.width, self.height = A4
        self.rect_width = 100 * mm
        self.rect_height = 70 * mm
        self.margin = 5 * mm
        self.upper_line_width = self.margin + 48 * mm

    def sender(self):
        if not self.sender_data:
            self.sender_data = []

        with open(self.sender_filename, 'r') as sender_txt:
            for line in sender_txt:
                self.sender_data.append(line.rstrip())

    def recipient(self):
        if not self.recipient_data:
            self.recipient_data = []
            with open(self.recipient_filename, 'r') as rec_txt:
                each_recipient = []
                for line in rec_txt:
                    if len(line.strip()) != 0:
                        each_recipient.append(line.rstrip())
                    else:
                        self.recipient_data.append(each_recipient)
                        each_recipient = []
                self.recipient_data.append(each_recipient)
            if len(self.recipient_data) > 8:
                print('Please max. 8 recipients each time!')

    def pdf_writer(self):
        self.recipient()
        self.sender()

        # TEXT
        text_conf = ['POTWIERDZENIE NADANIA', 'przesyłki poleconej nr', 'NADAWCA:', 'ODBIORCA:', self.kind,
                     'Opłata: ......... PLN', 'Masa: ........... g', 'Gabaryt: A[  ] B[  ]', 'Uwagi: .............']

        text_pos_x = 15
        text_pos_y = self.height - 23
        text_pos2_x = 200
        text_pos2_y = self.height - 86

        position_list = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3)]
        for pos in range(len(position_list) - len(self.recipient_data)):
            position_list.pop()

        for pos in position_list:
            # TEXT
            self.canvas.setFont("VeraBd", self.font_size)
            self.canvas.drawString(text_pos_x + self.rect_width * pos[0], text_pos_y - self.rect_height * pos[1],
                                   text_conf[0])
            self.canvas.setFont("Vera", self.font_size)
            self.canvas.drawString(text_pos_x + self.rect_width * pos[0], text_pos_y - 10 - self.rect_height * pos[1],
                                   text_conf[1])
            self.canvas.setFont("VeraBd", self.font_size)
            self.canvas.drawString(text_pos_x + self.rect_width * pos[0], text_pos_y - 26 - self.rect_height * pos[1],
                                   text_conf[2])
            self.canvas.setFont("VeraBd", self.font_size)
            self.canvas.drawString(text_pos_x + self.rect_width * pos[0], text_pos_y - 106 - self.rect_height * pos[1],
                                   text_conf[3])
            self.canvas.setFont("VeraBd", self.font_size)
            self.canvas.drawString(text_pos2_x + self.rect_width * pos[0], text_pos2_y - self.rect_height * pos[1],
                                   text_conf[4])
            self.canvas.setFont("Vera", self.font_size)
            self.canvas.drawString(text_pos2_x + self.rect_width * pos[0], text_pos2_y - 11 - self.rect_height * pos[1],
                                   text_conf[5])
            self.canvas.setFont("Vera", self.font_size)
            self.canvas.drawString(text_pos2_x + self.rect_width * pos[0], text_pos2_y - 22 - self.rect_height * pos[1],
                                   text_conf[6])
            self.canvas.setFont("Vera", self.font_size)
            self.canvas.drawString(text_pos2_x + self.rect_width * pos[0], text_pos2_y - 33 - self.rect_height * pos[1],
                                   text_conf[7])
            self.canvas.setFont("Vera", self.font_size)
            self.canvas.drawString(text_pos2_x + self.rect_width * pos[0], text_pos2_y - 44 - self.rect_height * pos[1],
                                   text_conf[8])
            # GEOMETRY
            # Left lower edge of the main rectangle (home)
            x_home = self.margin + self.rect_width * pos[0]
            y_home = self.height - self.margin - self.rect_height - self.rect_height * pos[1]

            # Main rectangle
            self.canvas.setDash(1, 2)
            self.canvas.setStrokeColor(gray)
            self.canvas.rect(x_home, y_home, self.rect_width, self.rect_height, stroke=1, fill=0)

            # Horizontal lines
            first_line_y = self.height - self.margin - 9 * mm - self.rect_height * pos[1]
            second_line_y = self.height - self.margin - 20 * mm - self.rect_height * pos[1]
            self.canvas.line(x_home,
                             first_line_y,
                             self.upper_line_width + self.rect_width * pos[0],
                             first_line_y)
            self.canvas.line(self.upper_line_width + self.rect_width * pos[0],
                             second_line_y,
                             self.width / 2 + self.rect_width * pos[0],
                             second_line_y)

            # Vertical lines
            self.canvas.line(self.upper_line_width + self.rect_width * pos[0],
                             self.height - self.margin - self.rect_height * pos[1],
                             self.upper_line_width + self.rect_width * pos[0],
                             second_line_y)
            self.canvas.line(self.margin + 65 * mm + self.rect_width * pos[0],
                             y_home,
                             self.margin + 65 * mm + self.rect_width * pos[0],
                             second_line_y)

            # Circle
            self.canvas.circle(self.margin + 82.5 * mm + self.rect_width * pos[0],
                               self.height - 61 * mm - self.rect_height * pos[1], 25, stroke=1, fill=0)

            # SENDER
            send_pos_x = 15 + self.rect_width * pos[0]
            send_pos_y = self.height - 59 - self.rect_height * pos[1]
            for line in self.sender_data:
                self.canvas.setFont("Vera", self.font_size)
                self.canvas.drawString(send_pos_x, send_pos_y, line)
                send_pos_y -= self.font_size + 1

        # RECIPIENT
        recipient_with_pos = list(zip(position_list, self.recipient_data))
        for word in recipient_with_pos:
            pos_x = 15 + self.rect_width * word[0][0]
            pos_y = self.height - 139 - self.rect_height * word[0][1]
            cur_recipient = word[1]
            for line in cur_recipient:
                self.canvas.setFont("Vera", self.font_size)
                self.canvas.drawString(pos_x, pos_y, line)
                pos_y -= self.font_size + 1

        self.canvas.save()


if __name__ == '__main__':
    ConfGenerator().pdf_writer()
