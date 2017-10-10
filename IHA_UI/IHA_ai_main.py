# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHA-ai_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
from IHA_ai_add_Entity import Ui_Form

class Ui_Form(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 238)
        Form.setAutoFillBackground(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.add_Entity_mainBtn = QtWidgets.QPushButton(Form)
        self.add_Entity_mainBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_Entity_mainBtn.setObjectName("add_Entity_mainBtn")
        self.verticalLayout.addWidget(self.add_Entity_mainBtn)
        self.add_Intent_mainBtn = QtWidgets.QPushButton(Form)
        self.add_Intent_mainBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_Intent_mainBtn.setObjectName("add_Intent_mainBtn")
        self.verticalLayout.addWidget(self.add_Intent_mainBtn)
        self.add_Command_mainBtn = QtWidgets.QPushButton(Form)
        self.add_Command_mainBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_Command_mainBtn.setAutoFillBackground(False)
        self.add_Command_mainBtn.setObjectName("add_Command_mainBtn")
        self.verticalLayout.addWidget(self.add_Command_mainBtn)
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IHA.ai"))
        self.add_Entity_mainBtn.setText(_translate("Form", "Add Entity"))
        self.add_Intent_mainBtn.setText(_translate("Form", "Add Intent"))
        self.add_Command_mainBtn.setText(_translate("Form", "Add Command"))
        self.exitBtn.setText(_translate("Form", "Exit"))
        self.add_Command_mainBtn.clicked.connect(self.add_Command_Function)
        self.add_Entity_mainBtn.clicked.connect(self.add_Entity_Function)
        self.add_Intent_mainBtn.clicked.connect(self.add_Intent_Function)
        self.exitBtn.clicked.connect(self.exit_Function)
        
    def add_Command_Function(self):
        print("add_Command")
    def add_Entity_Function(self):
        print("add_Entity")
    def add_Intent_Function(self):
        print("add_Intent")
    def exit_Function(self):
        print("Exit")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec_())
    
