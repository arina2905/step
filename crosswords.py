import sqlite3
import sys
from sqlite3 import Error

from PyQt5.QtWidgets import QInputDialog, QMessageBox

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QTextEdit

from PyQt5 import QtGui
from PyQt5.QtGui import QFont

DBNAME = 'Crosswords.db'


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


con = sqlite3.connect('Crosswords.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS question (
    id   INTEGER PRIMARY KEY AUTOINCREMENT
                 UNIQUE
                 NOT NULL,
    oset TEXT,
    rus  TEXT,
    img  BLOB
);
''')

con.commit()
con.close()
create_connection('Crosswords.db')

import sqlite3


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


# ф-ция добавления слов кроссворда в БД
def insert_blob(oset, rus, img):
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect(DBNAME)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO question
                                  (oset, rus, img) VALUES (?, ?, ?)"""

        img = convert_to_binary_data(img)
        # Преобразование данных в формат кортежа
        data_tuple = (oset, rus, img)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение добавлено в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


# insert_blob("дзул", "хлеб", "h12.jpg")


# insert_blob("лæг", "мужчина", "human.jpg")


# insert_blob('арс', 'медведь', 'h12.jpg')


# insert_blob('сæрд', 'лето', 'human.jpg')


# insert_blob('дон', 'вода', 'human.jpg')

# окошко с кроссвордом №1
class Crossword1(QMainWindow):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 600)
        self.setStyleSheet('background-color: #C19A6B')
        self.setWindowTitle('Дзырдбыдтæ')

        self.id_btn_1 = QPushButton(self)
        self.id_btn_1.setText('1')
        self.id_btn_1.setFont(QFont('Times', 25))
        self.id_btn_1.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.id_btn_1.resize(80, 80)
        self.id_btn_1.move(35, 120)

        self.id_btn_1.clicked.connect(self.input_w1)

        self.btn1_word1 = QPushButton(self)
        self.btn1_word1.setStyleSheet('QPushButton {background-color: #C19A6B')
        self.btn1_word1.setText('')
        self.btn1_word1.setFont(QFont('Times', 25))
        self.btn1_word1.resize(80, 80)
        self.btn1_word1.move(120, 120)

        self.btn2_word1 = QPushButton(self)
        self.btn2_word1.setText('')
        self.btn2_word1.setFont(QFont('Times', 25))
        self.btn2_word1.resize(80, 80)
        self.btn2_word1.move(200, 120)

        self.btn3_word1 = QPushButton(self)
        self.btn3_word1.setText('')
        self.btn3_word1.setFont(QFont('Times', 25))
        self.btn3_word1.resize(80, 80)
        self.btn3_word1.move(280, 120)

        self.btn4_word1 = QPushButton(self)
        self.btn4_word1.setText('')
        self.btn4_word1.setFont(QFont('Times', 25))
        self.btn4_word1.resize(80, 80)
        self.btn4_word1.move(360, 120)

        self.id_btn_2 = QPushButton(self)
        self.id_btn_2.setText('2')
        self.id_btn_2.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.id_btn_2.setFont(QFont('Times', 25))
        self.id_btn_2.resize(80, 80)
        self.id_btn_2.move(360, 35)

        self.id_btn_2.clicked.connect(self.input_w2)

        self.btn1_word2 = QPushButton(self)
        self.btn1_word2.setStyleSheet('QPushButton {background-color: #C19A6B')
        self.btn1_word2.setText('')
        self.btn1_word2.setFont(QFont('Times', 25))
        self.btn1_word2.resize(80, 80)
        self.btn1_word2.move(360, 120)

        self.btn2_word2 = QPushButton(self)
        self.btn2_word2.setText('')
        self.btn2_word2.setFont(QFont('Times', 25))
        self.btn2_word2.resize(80, 80)
        self.btn2_word2.move(360, 200)

        self.btn3_word2 = QPushButton(self)
        self.btn3_word2.setText('')
        self.btn3_word2.setFont(QFont('Times', 25))
        self.btn3_word2.resize(80, 80)
        self.btn3_word2.move(360, 280)

        self.btn_next = QPushButton(self)
        self.btn_next.setText('Фæстæмæ')
        self.btn_next.setStyleSheet('QPushButton {background-color: #673923}')
        self.btn_next.setFont(QFont('Times New Roman', 20))
        self.btn_next.resize(150, 50)
        self.btn_next.move(220, 500)

        self.btn_next.clicked.connect(self.back_crossword)

    def message(self):
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle('Рæдыд - ошибка')
        self.msg.setText('Фарст  æнæраст у! - Ответ неправильный!')

        self.msg.exec_()

    def input_w1(self):

        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute(f'''SELECT oset FROM question
                WHERE id = 1''')

        con.commit()
        con.close()

        if self.id_btn_1.sender():
            word1, ok_pressed = QInputDialog.getText(self, 'Введите слово на осетинском',
                                                     'Хлеб')

            if ok_pressed:
                if word1.lower() == 'дзул':
                    self.btn1_word1.setText(word1[0])
                    self.btn1_word1.setFont(QFont('Times', 25))
                    self.btn2_word1.setText(word1[1])
                    self.btn3_word1.setText(word1[2])
                    self.btn1_word2.setText(word1[3])
                else:
                    self.message()

    def input_w2(self):


        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute(f'''SELECT oset FROM question
                WHERE id = 2''')

        con.commit()
        con.close()

        if self.id_btn_2.sender():
            word2, ok_pressed = QInputDialog.getText(self, 'Введите слово на осетинском',
                                                     'Человек')

            if ok_pressed:
                if word2.capitalize() == 'Лæг':
                    self.btn1_word2.setText(word2[0])
                    self.id_btn_2.setStyleSheet('QPushButton {background-color: #8A6642}')
                    self.btn2_word2.setText(word2[1])
                    self.btn3_word2.setText(word2[2])
                else:
                    self.message()

    def back_crossword(self):
        self.parent.show()
        self.hide()


class Crossword2(QMainWindow):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setStyleSheet('background-color: #C19A6B')
        self.setWindowTitle('Дзырдбыдтæ')

        self.bakc = QPushButton(self)
        self.bakc.setText('Фæстæмæ')
        self.bakc.setStyleSheet('QPushButton {background-color: #673923}')
        self.bakc.setFont(QFont('Times New Roman', 20))
        self.bakc.resize(150, 50)
        self.bakc.move(220, 500)

        self.bakc.clicked.connect(self.back)

        self.id_btn_1 = QPushButton(self)
        self.id_btn_1.setText('1')
        self.id_btn_1.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.id_btn_1.setFont(QFont('Times', 25))
        self.id_btn_1.resize(80, 80)
        self.id_btn_1.move(35, 120)

        self.id_btn_1.clicked.connect(self.input_w1)

        self.btn1_word1 = QPushButton(self)
        self.btn1_word1.setText('')
        self.btn1_word1.setFont(QFont('Times', 25))
        self.btn1_word1.resize(80, 80)
        self.btn1_word1.move(120, 120)

        self.btn2_word1 = QPushButton(self)
        self.btn2_word1.setText('')
        self.btn2_word1.setFont(QFont('Times', 25))
        self.btn2_word1.resize(80, 80)
        self.btn2_word1.move(200, 120)

        self.btn3_word1 = QPushButton(self)
        self.btn3_word1.setText('')
        self.btn3_word1.setFont(QFont('Times', 25))
        self.btn3_word1.resize(80, 80)
        self.btn3_word1.move(280, 120)

        self.id_btn_2 = QPushButton(self)
        self.id_btn_2.setText('2')
        self.id_btn_2.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.id_btn_2.setFont(QFont('Times', 25))
        self.id_btn_2.resize(80, 80)
        self.id_btn_2.move(280, 35)

        self.id_btn_2.clicked.connect(self.input_w2)

        self.btn1_word2 = QPushButton(self)
        self.btn1_word2.setText('')
        self.btn1_word2.setFont(QFont('Times', 25))
        self.btn1_word2.resize(80, 80)
        self.btn1_word2.move(280, 120)

        self.btn2_word2 = QPushButton(self)
        self.btn2_word2.setText('')
        self.btn2_word2.setFont(QFont('Times', 25))
        self.btn2_word2.resize(80, 80)
        self.btn2_word2.move(280, 200)

        self.btn3_word2 = QPushButton(self)
        self.btn3_word2.setText('')
        self.btn3_word2.setFont(QFont('Times', 25))
        self.btn3_word2.resize(80, 80)
        self.btn3_word2.move(280, 280)

        self.btn4_word2 = QPushButton(self)
        self.btn4_word2.setText('')
        self.btn4_word2.setFont(QFont('Times', 25))
        self.btn4_word2.resize(80, 80)
        self.btn4_word2.move(280, 360)

        self.id_btn_3 = QPushButton(self)
        self.id_btn_3.setText('3')
        self.id_btn_3.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.id_btn_3.setFont(QFont('Times', 25))
        self.id_btn_3.resize(80, 80)
        self.id_btn_3.move(195, 360)

        self.id_btn_3.clicked.connect(self.input_w3)

        self.btn1_word3 = QPushButton(self)
        self.btn1_word3.setText('')
        self.btn1_word3.setFont(QFont('Times', 25))
        self.btn1_word3.resize(80, 80)
        self.btn1_word3.move(280, 360)

        self.btn2_word3 = QPushButton(self)
        self.btn2_word3.setText('')
        self.btn2_word3.setFont(QFont('Times', 25))
        self.btn2_word3.resize(80, 80)
        self.btn2_word3.move(360, 360)

        self.btn3_word3 = QPushButton(self)
        self.btn3_word3.setText('')
        self.btn3_word3.setFont(QFont('Times', 25))
        self.btn3_word3.resize(80, 80)
        self.btn3_word3.move(440, 360)

    def message(self):
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle('Рæдыд - ошибка')
        self.msg.setText('Фарст  æнæраст у! - Ответ неправильный!')

        x = self.msg.exec_()

    def input_w1(self):
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        s3 = f'''SELECT oset FROM question
                        WHERE id = 3'''
        cur.execute(s3).fetchone()
        con.commit()
        con.close()

        if self.id_btn_1.sender():
            word1, ok_pressed = QInputDialog.getText(self, 'Введите слово на осетинском',
                                                     'Медведь')

            if ok_pressed:
                if word1.lower() == 'арс':
                    self.btn1_word1.setText(word1[0])
                    self.btn2_word1.setText(word1[1])
                    self.btn1_word2.setText(word1[2])
                else:
                    self.message()

    def input_w2(self):
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute(f'''SELECT oset FROM question
                                WHERE id = 4''')

        con.commit()
        con.close()
        if self.id_btn_2.sender():
            word2, ok_pressed = QInputDialog.getText(self, 'Введите слово на осетинском',
                                                     'Лето')
            print(word2[:4])

            if ok_pressed:
                if word2.capitalize() == 'Сæрд':
                    self.btn1_word2.setText(word2[0])
                    self.btn2_word2.setText(word2[1])
                    self.btn3_word2.setText(word2[2])
                    self.btn1_word3.setText(word2[3])
                else:
                    self.message()

    def input_w3(self):
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute(f'''SELECT oset FROM question
                                        WHERE id = 5''')

        con.commit()
        con.close()
        if self.id_btn_3.sender():
            word3, ok_pressed = QInputDialog.getText(self, 'Введите слово на осетинском',
                                                     'Вода')

            if ok_pressed:
                if word3.capitalize() == 'Дон':
                    self.btn1_word3.setText(word3[0])
                    self.btn2_word3.setText(word3[1])
                    self.btn3_word3.setText(word3[2])
                else:
                    self.message()

    def back(self):
        self.parent.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exx = Crossword1()
    exx.show()
    ex = Crossword2()
    sys.exit(app.exec_())
