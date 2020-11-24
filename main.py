import sys
import random as rd

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QBrush, QPen, QPainter


class YellowCycles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('ui')
        self.ok = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.ok != 0:
            self.drawCycles(qp)
        qp.end()

    def drawCycles(self, qp):
        for i in range(200):
            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)
            x = rd.randint(0, 800)
            y = rd.randint(0, 700)
            height = rd.randint(10, 257)
            qp.setBrush(QColor(r, g, b))
            qp.setPen(QColor(r, g, b))
            qp.drawEllipse(x, y, height, height)

    def draw(self):
        self.ok = 1
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = YellowCycles()
    widget.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())