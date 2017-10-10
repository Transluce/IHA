# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHA-ai_add_Entity.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget

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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.entity_highlighted = QtWidgets.QLabel(Form)
        self.entity_highlighted.setObjectName("entity_highlighted")
        self.horizontalLayout_4.addWidget(self.entity_highlighted, 0, QtCore.Qt.AlignLeft)
        self.intents_combo = QtWidgets.QComboBox(Form)
        self.intents_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.intents_combo.setObjectName("intents_combo")
        self.horizontalLayout_4.addWidget(self.intents_combo, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addEntity_btn = QtWidgets.QPushButton(Form)
        self.addEntity_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addEntity_btn.setObjectName("addEntity_btn")
        self.horizontalLayout.addWidget(self.addEntity_btn, 0, QtCore.Qt.AlignTop)
        self.addEntity_lineEdit = QtWidgets.QLineEdit(Form)
        self.addEntity_lineEdit.setEnabled(True)
        self.addEntity_lineEdit.setObjectName("addEntity_lineEdit")
        self.horizontalLayout.addWidget(self.addEntity_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.validate_btn = QtWidgets.QPushButton(Form)
        self.validate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.validate_btn.setObjectName("validate_btn")
        self.horizontalLayout_2.addWidget(self.validate_btn, 0, QtCore.Qt.AlignLeft)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IHA.ai"))
        self.entity_highlighted.setText(_translate("Form", "TextLabel"))
        self.addEntity_btn.setText(_translate("Form", "Add Entity"))
        self.validate_btn.setText(_translate("Form", "Validate"))
        self.cancel_btn.setText(_translate("Form", "Cancel"))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec_())