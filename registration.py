import sys
import sqlite3

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from sqlite3 import Error


from go_to_cross import ToCrosswords

DBNAME = 'Users.db'


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


con = sqlite3.connect('Users.db')
cur = con.cursor()
cur.execute(f'''CREATE TABLE IF NOT EXISTS Users(
    id      INTEGER PRIMARY KEY AUTOINCREMENT
                    NOT NULL
                    UNIQUE,
    name    TEXT,
    age     INTEGER,
    login TEXT UNIQUE NOT NULL, 
    password TEXT UNIQUE NOT NULL
);
            ''')

con.commit()
con.close()
create_connection('Users.db')


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.enter = Enter(self)
        self.initUI()

    # окошко регистрации
    def initUI(self):
        self.setFixedHeight(310)
        self.setStyleSheet('background-color: #C19A6B')
        self.setFixedWidth(390)

        self.setWindowTitle('Регистраци')

        lay = QVBoxLayout(self)

        self.name = QLabel('Ном', self)
        self.name.setFont(QFont('Times New Roman', 15))
        self.name.move(50, 25)

        self.login = QLabel('Логин', self)
        self.login.setFont(QtGui.QFont('Times New Roman', 15))
        self.login.move(38, 55)

        self.password = QLabel('Пароль', self)
        self.password.setFont(QFont('Times New Roman', 15))
        self.password.move(25, 85)

        self.country = QLabel('Бæстæ', self)
        self.country.setFont(QFont('Times New Roman', 15))
        self.country.move(25, 114)

        self.age = QLabel('Кар', self)
        self.age.setFont(QFont('Times New Roman', 15))
        self.age.move(50, 145)

        self.gender = QLabel("Ӕрд", self)
        self.gender.setFont(QFont('Times New Roman', 15))
        self.gender.move(50, 178)

        self.input_name = QLineEdit(self)
        self.input_name.setFont(QFont('Times', 12))
        self.input_name.setFixedSize(180, 23)
        self.input_name.move(100, 30)

        self.input_login = QLineEdit(self)
        self.input_login.setFont(QFont('Times', 12))
        self.input_login.setFixedSize(180, 23)
        self.input_login.move(100, 60)

        self.input_password = QLineEdit(self)
        self.input_password.setFont(QFont('Times', 12))
        self.input_password.setFixedSize(180, 23)
        self.input_password.move(100, 90)

        self.input_country = QComboBox(self)
        self.input_country.resize(180, 23)
        self.input_country.setFont(QFont('Times', 12))
        self.input_country.move(100, 120)
        self.input_country.addItem('Равзарут уæ бæстæ:D')
        self.input_country.addItem('Россия')
        self.input_country.addItem('Уæрæсе')
        self.input_country.addItem('Russia')
        self.input_country.addItem('Rusia')

        self.input_age = QLineEdit(self)
        self.login.setFont(QFont('Times', 12))
        self.input_age.setFixedSize(180, 23)
        self.input_age.move(100, 150)

        self.layout = QHBoxLayout(self)

        self.select_gender_M = QRadioButton(self)
        self.select_gender_M.setText('Нæлыстæг')
        self.select_gender_M.setFont(QFont('Times', 12))
        self.select_gender_M.move(100, 180)
        self.select_gender_M.setChecked(False)
        self.select_gender_M.toggled.connect(lambda: self.btnstate(self.select_gender_M))

        self.layout.addWidget(self.select_gender_M)

        self.select_gender_W = QRadioButton(self)
        self.select_gender_W.setText('Силæрдæ')
        self.select_gender_W.setFont(QFont('Times', 13))
        self.select_gender_W.move(205, 180)
        self.select_gender_W.setChecked(False)
        self.select_gender_W.toggled.connect(lambda: self.btnstate(self.select_gender_W))

        self.layout.addWidget(self.select_gender_W)

        self.setLayout(self.layout)

        self.registration = QPushButton(self)
        self.registration.setText('Регистрацигонд æрцæуын')
        self.registration.setStyleSheet('QPushButton {background-color: #673923}')
        self.registration.setFont(QFont('Times New Roman', 12))
        self.registration.resize(220, 30)
        self.registration.move(40, 250)
        self.registration.clicked.connect(self.addUser)

        self.ente = QPushButton(self)
        self.ente.setText('Бацæуын')
        self.ente.setStyleSheet('QPushButton {background-color: #673923}')
        self.ente.setFont(QFont('Times New Roman', 12))
        self.ente.resize(85, 30)
        self.ente.move(265, 250)
        self.ente.clicked.connect(self.reg_ok)

    def reg_ok(self):
        self.enter.show()
        self.hide()

    # ф-ция проверки того, на какую радиокнопку нажали
    def btnstate(self, b):
        if b.text == 'Нæлыстæг':
            if b.isChecked() == True:
                print(b.text() + " is selected")
            else:
                print('Female is selected')

        if b.text() == "Силæрдæ":
            if b.isChecked() == True:
                print(b.text() + " is selected")
            else:
                print('Male is selected')

    # ф-ция добавления пользователя в БД
    def addUser(self):
        self.name = self.input_name.text()
        self.age = self.input_age.text()
        self.login = self.input_login.text()
        self.password = self.input_password.text()
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        try:
            s = f'''INSERT INTO User
            (name, age, login, password) VALUES (
                "{self.name}", 
                "{self.age}", 
                "{self.login}", 
                "{self.password}"
                )'''
            print(s)
            cur.execute(s)
            con.commit()
            con.close()
        except Exception:
            print(Exception.__name__)


class Enter(QWidget):
    def __init__(self, parent):
        self.parent = parent
        self.next = ToCrosswords(self)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedHeight(180)
        self.setFixedWidth(230)
        self.setWindowTitle('Бацæуæн')
        self.setStyleSheet('background-color: #C19A6B')


        self.login = QLabel('Логин', self)
        self.login.setFont(QFont('Times New Roman', 15))
        self.login.move(35, 30)

        self.password = QLabel('Пароль', self)
        self.password.setFont(QFont('Times New Roman', 15))
        self.password.move(27, 66)

        self.input_login = QLineEdit(self)
        self.input_login.setFixedSize(110, 25)
        self.input_login.move(100, 30)

        self.input_password = QLineEdit(self)
        self.input_password.setFixedSize(110, 25)
        self.input_password.move(100, 65)

        self.inreg = QPushButton(self)
        self.inreg.setText('Бацæуын')
        self.inreg.setFont(QFont('Times New Roman', 15))
        self.inreg.setStyleSheet('background-color: #673923')

        self.inreg.resize(130, 35)
        self.inreg.move(50, 115)
        self.inreg.clicked.connect(self.check_user)

    def trans_inreg(self):
        self.next.show()
        self.hide()

    def check_user(self):
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        self.login = self.input_login.text()
        try:
            s = f'''SELECT login, password FROM User
            WHERE login = "{self.login}"'''
            print(s)
            res = cur.execute(s).fetchone()
            print(res)
            login, password = res

            con.commit()
            con.close()
            if self.login == login \
                and self.input_password.text() == password:
                self.trans_inreg()
        except Exception:
            print(Exception.__name__)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration()
    ex.show()
    sys.exit(app.exec_())
