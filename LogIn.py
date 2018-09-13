# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Registration import Ui_Registration

class ClickableLineEdit(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal() 
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton: self.clicked.emit()

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(630, 507)
        LogIn.setFixedSize(630, 507)
        self.pushButtonLogin = QtWidgets.QPushButton(LogIn)
        self.pushButtonLogin.setGeometry(QtCore.QRect(320, 340, 290, 51))
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.lineEditUsername = ClickableLineEdit(LogIn)
        self.lineEditUsername.setGeometry(QtCore.QRect(320, 220, 290, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = ClickableLineEdit(LogIn)
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 260, 290, 31))
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonCreateAccount = QtWidgets.QPushButton(LogIn)
        self.pushButtonCreateAccount.setGeometry(QtCore.QRect(320, 402, 290, 31))
        self.pushButtonCreateAccount.setObjectName("pushButtonCreateAccount")
        font.setPointSize(15)
        self.pushButtonLogin.setFont(font)
        self.label = QtWidgets.QLabel(LogIn)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.labelMapuaLogo = QtWidgets.QLabel(LogIn)
        self.labelMapuaLogo.setObjectName("labelMapuaLogo")
        self.labelMapuaLogo.setGeometry(390,45,150,150)
        pic = QtGui.QPixmap("MapuaLogo.png")
        self.labelMapuaLogo.setPixmap(pic)
        self.emptyUsername = True
        self.emptyPassword = True
        LogIn.setStyleSheet(open("Design.qss",'r').read())
        self.lineEditUsername.setStyleSheet("color: gray")
        self.lineEditUsername.setText("someone@mymail.mapua.edu.ph")
        self.lineEditPassword.setStyleSheet("color: gray")
        self.lineEditPassword.setText("Password")
        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        LogIn.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        LogIn.setTabOrder(self.lineEditPassword, self.pushButtonLogin)
        LogIn.setTabOrder(self.pushButtonLogin, self.pushButtonCreateAccount)
        self.lineEditUsername.setCursorPosition(0)
        LogIn.setWindowIcon(QtGui.QIcon("MapuaIcon.png"))
        
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Mapua University"))
        self.pushButtonLogin.setText(_translate("LogIn", "LOGIN"))
        self.pushButtonCreateAccount.setText(_translate("LogIn", "REGISTER"))
        self.label.setText(_translate("LogIn", "<html><head/><body><p>Welcome </p><p>to the</p><p>Student Council </p><p>Election</p></body></html>"))
        self.lineEditUsername.textEdited.connect(self.removeUsername)
        self.lineEditPassword.textEdited.connect(self.removePassword)
        self.pushButtonLogin.clicked.connect(self.logIn)
        self.pushButtonCreateAccount.clicked.connect(self.createAccount)
        self.lineEditUsername.clicked.connect(self.usernameClicked)
        self.lineEditUsername.editingFinished.connect(self.resetUsername)
        self.lineEditPassword.clicked.connect(self.passwordCLicked)
        self.lineEditPassword.editingFinished.connect(self.resetPassword)
        self.pushButtonCreateAccount.mouseMoveEvent   
        
    def logIn(self):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle("SUCCESS")
        mess.setText("WELCOME")
        mess.setWindowIcon(QtGui.QIcon("icon.png"))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def createAccount(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Registration = QtWidgets.QWidget()
        ui = Ui_Registration()
        ui.setupUi(self.Registration)
        self.Registration.show()
        
    def removeUsername(self):
        if self.emptyUsername:
            self.emptyUsername = False
            self.lineEditUsername.setStyleSheet("color: white;")
            self.lineEditUsername.setText(self.lineEditUsername.text()[0])     
    def removePassword(self):
        if self.emptyPassword:
            self.emptyPassword = False
            self.lineEditPassword.setStyleSheet("color: white;")
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEditPassword.setText(self.lineEditPassword.text()[0])
            
    def resetUsername(self):
        if len(self.lineEditUsername.text()) == 0:
            self.emptyUsername = True
        if self.emptyUsername:
            self.lineEditUsername.setStyleSheet("color: gray;")
            self.lineEditUsername.setText("someone@mymail.mapua.edu.ph") 
    def resetPassword(self):
        if len(self.lineEditPassword.text()) == 0:
            self.emptyPassword = True
        if self.emptyPassword:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassword.setStyleSheet("color: gray;")
            self.lineEditPassword.setText("Password")
            
    def usernameClicked(self):
        if self.lineEditUsername.text() == "someone@mymail.mapua.edu.ph":
            self.lineEditUsername.setCursorPosition(0)
        
    def passwordCLicked(self):
        if self.lineEditPassword.text() == "Password":
            self.lineEditPassword.setCursorPosition(0)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())

