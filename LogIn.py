# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(579, 507)
        LogIn.setFixedSize(579, 507)
        self.pushButtonLogin = QtWidgets.QPushButton(LogIn)
        self.pushButtonLogin.setGeometry(QtCore.QRect(320, 340, 221, 51))
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.lineEditUsername = QtWidgets.QLineEdit(LogIn)
        self.lineEditUsername.setGeometry(QtCore.QRect(320, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(LogIn)
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPassword.setFont(font)
        font.setPointSize(10)
        self.pushButtonLogin.setFont(font)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonCreateAccount = QtWidgets.QPushButton(LogIn)
        self.pushButtonCreateAccount.setGeometry(QtCore.QRect(320, 402, 221, 31))
        self.pushButtonCreateAccount.setObjectName("pushButtonCreateAccount")
        font.setPointSize(10)
        self.pushButtonCreateAccount.setFont(font)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        LogIn.setStyleSheet(open("LogInDesign.qss",'r').read())
        
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Form"))
        self.pushButtonLogin.setText(_translate("LogIn", "LOGIN"))
        self.pushButtonCreateAccount.setText(_translate("LogIn", "CREATE ACCOUNT"))
        self.lineEditUsername.textEdited.connect(self.remove)
        self.pushButtonLogin.clicked.connect(self.login)
        self.pushButtonCreateAccount.clicked.connect(self.createaccount)
        
    def login(self):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle("SUCCESS")
        mess.setText("WELCOME")
        mess.setWindowIcon(QtGui.QIcon("icon.png"))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def createaccount(self):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle("SUCCESS")
        mess.setText("WELCOME")
        mess.setWindowIcon(QtGui.QIcon("icon.png"))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def remove(self):
        self.lineEditPassword.setText("saw")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())


