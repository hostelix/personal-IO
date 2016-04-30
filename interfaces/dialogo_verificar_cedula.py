# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_verificacion_cedula.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(322, 238)
        Dialog.setStyleSheet(_fromUtf8("#input_cedula{background-color: white;}\n"
                                       "#label_cedula{font-size: 15px;}"))
        self.btn_aceptar = QtGui.QPushButton(Dialog)
        self.btn_aceptar.setGeometry(QtCore.QRect(90, 150, 141, 41))
        self.btn_aceptar.setObjectName(_fromUtf8("btn_aceptar"))
        self.input_cedula = QtGui.QLineEdit(Dialog)
        self.input_cedula.setGeometry(QtCore.QRect(60, 80, 201, 31))
        self.input_cedula.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_cedula.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cedula.setPlaceholderText(_fromUtf8(""))
        self.input_cedula.setObjectName(_fromUtf8("input_cedula"))
        self.label_cedula = QtGui.QLabel(Dialog)
        self.label_cedula.setGeometry(QtCore.QRect(50, 40, 361, 21))
        self.label_cedula.setObjectName(_fromUtf8("label_cedula"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Verificacion Cedula", None))
        self.btn_aceptar.setText(_translate("Dialog", "Aceptar", None))
        self.label_cedula.setText(_translate("Dialog", "Introduzca su cedula de Identidad", None))
