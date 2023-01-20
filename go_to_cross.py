import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from crosswords import Crossword1, Crossword2


class ToCrosswords(QMainWindow):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.crossword_1 = Crossword1(self)
        self.crossowrd_2 = Crossword2(self)
        self.initUI()

    def initUI(self):
        self.setFixedHeight(180)
        self.setFixedWidth(200)
        self.setStyleSheet('background-color: #C19A6B')
        self.setWindowTitle('Равзарут дзырдбыд')

        self.cross1 = QPushButton(self)
        self.cross1.setText('Дзырдбыд_1')
        self.cross1.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.cross1.setFont(QFont('Times', 15))
        self.cross1.resize(180, 50)
        self.cross1.move(10, 10)

        self.cross1.clicked.connect(self.cr1)

        self.cross2 = QPushButton(self)
        self.cross2.setText('Дзырдбыд_2')
        self.cross2.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.cross2.setFont(QFont('Times', 15))
        self.cross2.resize(180, 50)
        self.cross2.move(10, 60)

        self.cross2.clicked.connect(self.cr2)

        self.back = QPushButton(self)
        self.back.setText('Фæстæмæ')
        self.back.setStyleSheet('QPushButton {background-color: #673923}')
        self.back.setFont(QFont('Times New Roman', 15))
        self.back.resize(120, 30)
        self.back.move(40, 120)

        self.back.clicked.connect(self.to_return)


    def cr1(self):
        self.crossword_1.show()
        self.hide()


    def cr2(self):
        self.crossowrd_2.show()
        self.hide()


    def to_return(self):
        self.parent.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToCrosswords()
    ex.show()
    sys.exit(app.exec_())
