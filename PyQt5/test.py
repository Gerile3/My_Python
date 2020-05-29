import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("Test")
    win.setGeometry(200, 200, 500, 500)
    win.setWindowIcon(QIcon('test.png'))
    win.setToolTip("This is test")

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
