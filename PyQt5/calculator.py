import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainForm(QMainWindow):
    """Basic Calculator app"""
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator v0.1')
        self.setWindowIcon(QIcon('test.png'))
        self.setGeometry(200, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('First Number: ')
        self.lbl_num1.move(50, 30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150, 30)
        self.txt_num1.resize(200, 32)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Second Number: ')
        self.lbl_num2.move(50, 80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150, 80)
        self.txt_num2.resize(200, 32)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText('+')
        self.btn_add.move(150, 130)
        self.btn_add.clicked.connect(self.calculation)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText('-')
        self.btn_sub.move(150, 170)
        self.btn_sub.clicked.connect(self.calculation)

        self.btn_multp = QtWidgets.QPushButton(self)
        self.btn_multp.setText('*')
        self.btn_multp.move(150, 210)
        self.btn_multp.clicked.connect(self.calculation)

        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText('/')
        self.btn_division.move(150, 250)
        self.btn_division.clicked.connect(self.calculation)

        self.lbl_operations = QtWidgets.QLabel(self)
        self.lbl_operations.setText('Operations')
        self.lbl_operations.move(50, 130)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Result')
        self.lbl_result.move(150, 290)

    def calculation(self):
        sender = self.sender().text()
        result = 0

        if sender == '+':
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == '-':
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == '*':
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == '/':
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())

        self.lbl_result.setText('Result = ' + str(result))


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
