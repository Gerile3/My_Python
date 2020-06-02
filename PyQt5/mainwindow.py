# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num1 = QtWidgets.QLabel(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(70, 70, 47, 13))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLabel(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(70, 90, 47, 51))
        self.num2.setObjectName("num2")
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.btn_calculate.setObjectName("btn_calculate")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(270, 80, 51, 31))
        self.result.setObjectName("result")
        self.result_show = QtWidgets.QLabel(self.centralwidget)
        self.result_show.setGeometry(QtCore.QRect(310, 30, 131, 131))
        self.result_show.setObjectName("result_show")
        self.num1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.num1_input.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.num1_input.setObjectName("num1_input")
        self.num2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.num2_input.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.num2_input.setObjectName("num2_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num1.setText(_translate("MainWindow", "Number 1"))
        self.num2.setText(_translate("MainWindow", "Number 2"))
        self.btn_calculate.setText(_translate("MainWindow", "Calculate"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.result_show.setText(_translate("MainWindow", "TextLabel"))
