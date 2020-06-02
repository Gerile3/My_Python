import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow


class MainForm(QMainWindow):
    """Basic Calculator app"""
    def __init__(self):
        super(MainForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_calculate.clicked.connect(self.calculation)

    def calculation(self):
        result = ""

        for i in range(4):
            if i == 0:
                result += str(int(self.ui.num1_input.text()) + int(self.ui.num2_input.text())) + "\n"
            if i == 1:
                result += str(int(self.ui.num1_input.text()) - int(self.ui.num2_input.text())) + "\n"
            if i == 2:
                result += str(int(self.ui.num1_input.text()) * int(self.ui.num2_input.text())) + "\n"
            if i == 3:
                result += str(int(self.ui.num1_input.text()) / int(self.ui.num2_input.text())) + "\n"

            self.ui.result_show.setText(result)


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
