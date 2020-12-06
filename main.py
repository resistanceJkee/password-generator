import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random as rand
import pyperclip
from screeninfo import get_monitors


def get_width():
    return get_monitors()[0].width


def get_height():
    return get_monitors()[0].height


class PassRand(QWidget):

    ql = ""

    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.resize(550, 100)
        self.add_widgets()
        """
        500/2 - центрирует по горизонтали
        100 не делю на 2, чтобы чуть повыше было
        """
        self.move(int(get_width()/2 - 550/2),
                  int(get_height()/2) - 100)
        self.setWindowTitle("Password Randomizer")
        self.show()

    def add_widgets(self):
        q = QLineEdit(self)
        q.resize(450, 100)
        q.move(0, 0)
        q.setFont(QFont("Ubuntu", 14))
        q.textChanged[str].connect(self.copy_text)
        q.setAlignment(Qt.AlignCenter)
        self.ql = q
        btn = QPushButton(self)
        btn.resize(100, 50)
        btn.move(550-100, 25)
        btn.setText("Generate")
        btn.setFont(QFont("Ubuntu", 12))
        btn.clicked.connect(self.generate_text)
        self.generate_text()

    def generate_text(self):
        sym = 'abc+d1ef-ghij/kln2op*qrs3t!uvw&xy4zA$5BC#D6EF?GHI7JK=LMN8OP@QRS>T9UVWX<Y0Z'
        data = ""
        for i in range(15):
            data += str(sym[rand.randint(0, 73)])
        self.ql.setText(data)

    def copy_text(self, text):
        pyperclip.copy(text)


def main():
    app = QApplication(sys.argv)
    pr = PassRand()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()