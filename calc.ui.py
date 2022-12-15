# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 390)
        MainWindow.setStyleSheet("background-color: rgb(97, 92, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"background-color: rgb(177, 177, 177);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(0, 260, 150, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn0.setObjectName("btn0")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(150, 260, 91, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_result.setFont(font)
        self.btn_result.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 85, 0);")
        self.btn_result.setObjectName("btn_result")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(0, 50, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(228, 255, 88);\n"
"background-color: rgb(255, 170, 0);")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(80, 50, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: rgb(228, 255, 88);\n"
"background-color: rgb(255, 170, 0);")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(160, 50, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(0, 120, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(80, 120, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(160, 120, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(0, 190, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(80, 190, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(160, 190, 81, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn9.setObjectName("btn9")
        self.btn5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5_2.setGeometry(QtCore.QRect(240, 50, 50, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn5_2.setFont(font)
        self.btn5_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn5_2.setObjectName("btn5_2")
        self.btn5_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5_3.setGeometry(QtCore.QRect(240, 130, 50, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn5_3.setFont(font)
        self.btn5_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn5_3.setObjectName("btn5_3")
        self.btn5_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5_4.setGeometry(QtCore.QRect(240, 200, 50, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn5_4.setFont(font)
        self.btn5_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn5_4.setObjectName("btn5_4")
        self.btn5_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5_5.setGeometry(QtCore.QRect(240, 270, 50, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn5_5.setFont(font)
        self.btn5_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn5_5.setObjectName("btn5_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 290, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.is_equal = False
        self.add_function()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn5_2.setText(_translate("MainWindow", "+"))
        self.btn5_3.setText(_translate("MainWindow", "-"))
        self.btn5_4.setText(_translate("MainWindow", "x"))
        self.btn5_5.setText(_translate("MainWindow", "/"))


    def add_function(self):     #коннектим кнопки
            self.btn0.clicked.connect(lambda: self.write_number(self.btn0.text()))
            self.btn1.clicked.connect(lambda: self.write_number(self.btn1.text()))
            self.btn2.clicked.connect(lambda: self.write_number(self.btn2.text()))
            self.btn3.clicked.connect(lambda: self.write_number(self.btn3.text()))
            self.btn4.clicked.connect(lambda: self.write_number(self.btn4.text()))
            self.btn5.clicked.connect(lambda: self.write_number(self.btn5.text()))
            self.btn6.clicked.connect(lambda: self.write_number(self.btn6.text()))
            self.btn7.clicked.connect(lambda: self.write_number(self.btn7.text()))
            self.btn8.clicked.connect(lambda: self.write_number(self.btn8.text()))
            self.btn9.clicked.connect(lambda: self.write_number(self.btn9.text()))
            self.btn5_2.clicked.connect(lambda: self.write_number(self.btn5_2.text()))
            self.btn5_3.clicked.connect(lambda: self.write_number(self.btn5_3.text()))
            self.btn5_4.clicked.connect(lambda: self.write_number(self.btn5_4.text()))
            self.btn5_5.clicked.connect(lambda: self.write_number(self.btn5_5.text()))

            self.btn_result.clicked.connect(self.results)


    def write_number(self, number):     #пишем кнопки на панель label
        if self.label_result.text() == '0' or self.is_equal == True:
                self.label_result.setText(number)
                self.is_equal = False
        else:
                self.label_result.setText(self.label_result.text() + number)


    def results(self):
            if not self.is_equal:
                res = eval(self.label_result.text())
                self.label_result.setText('Результат: ' + str(res))
                self.is_equal = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
