# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 458)
        self.pB_previous = QtWidgets.QPushButton(Form)
        self.pB_previous.setGeometry(QtCore.QRect(522, 19, 40, 40))
        self.pB_previous.setObjectName("pB_previous")
        self.pB_next = QtWidgets.QPushButton(Form)
        self.pB_next.setGeometry(QtCore.QRect(572, 20, 40, 40))
        self.pB_next.setObjectName("pB_next")
        self.lineEdit_page = QtWidgets.QLineEdit(Form)
        self.lineEdit_page.setGeometry(QtCore.QRect(32, 20, 151, 41))
        self.lineEdit_page.setStyleSheet("font: 16pt \"黑体\";")
        self.lineEdit_page.setObjectName("lineEdit_page")
        self.lineEdit_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_path.setGeometry(QtCore.QRect(197, 20, 311, 41))
        self.lineEdit_path.setStyleSheet("font: 16pt \"黑体\";")
        self.lineEdit_path.setText("")
        self.lineEdit_path.setObjectName("lineEdit_path")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pB_previous.setText(_translate("Form", "↑"))
        self.pB_next.setText(_translate("Form", "↓"))
