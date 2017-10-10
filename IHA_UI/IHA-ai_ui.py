# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHA-ai.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget

class Ui_Form(QWidget):
    
    def __init__(self):
        #QtGui.QWidget.__init__(self)
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 248)
        Form.setMinimumSize(QtCore.QSize(20, 40))
        self.word_Highlighted = QtWidgets.QLabel(Form)
        self.word_Highlighted.setGeometry(QtCore.QRect(10, 50, 300, 41))
        self.word_Highlighted.setMinimumSize(QtCore.QSize(300, 20))
        self.word_Highlighted.setObjectName("word_Highlighted")
        self.validate_btn = QtWidgets.QPushButton(Form)
        self.validate_btn.setGeometry(QtCore.QRect(10, 210, 150, 25))
        self.validate_btn.setMinimumSize(QtCore.QSize(150, 20))
        self.validate_btn.setMaximumSize(QtCore.QSize(150, 25))
        self.validate_btn.setObjectName("validate_btn")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 481, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(318, 60, 171, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IHA.ai"))
        self.word_Highlighted.setText(_translate("Form", "Highlighted Word"))
        self.validate_btn.setText(_translate("Form", "Validate"))
        self.validate_btn.clicked.connect(self.validateFunction)
        
    
    def validateFunction(self):
        
        sender= self.sender()
        if sender.text() == 'Validate':
            print(self.lineEdit.text())
            #print("Validated")
        else:
            self.lineEdit.clear()
       

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec_())
