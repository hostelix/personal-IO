# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_verificacion_usuario.ui'
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


class Ui_DialogoVerificarAdmin(object):
    def setupUi(self, DialogoVerificarAdmin):
        DialogoVerificarAdmin.setObjectName(_fromUtf8("DialogoVerificarAdmin"))
        DialogoVerificarAdmin.resize(380, 273)
        self.btn_verificar = QtGui.QPushButton(DialogoVerificarAdmin)
        self.btn_verificar.setGeometry(QtCore.QRect(130, 210, 101, 41))
        self.btn_verificar.setObjectName(_fromUtf8("btn_verificar"))
        self.label_usuario = QtGui.QLabel(DialogoVerificarAdmin)
        self.label_usuario.setGeometry(QtCore.QRect(150, 40, 59, 17))
        self.label_usuario.setStyleSheet(_fromUtf8("font-size:18px;\n"
                                                   ""))
        self.label_usuario.setObjectName(_fromUtf8("label_usuario"))
        self.input_usuario = QtGui.QLineEdit(DialogoVerificarAdmin)
        self.input_usuario.setGeometry(QtCore.QRect(80, 70, 211, 31))
        self.input_usuario.setObjectName(_fromUtf8("input_usuario"))
        self.input_password = QtGui.QLineEdit(DialogoVerificarAdmin)
        self.input_password.setGeometry(QtCore.QRect(80, 150, 211, 31))
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.label_oassword = QtGui.QLabel(DialogoVerificarAdmin)
        self.label_oassword.setGeometry(QtCore.QRect(140, 120, 101, 20))
        self.label_oassword.setStyleSheet(_fromUtf8("font-size:18px;\n"
                                                    ""))
        self.label_oassword.setObjectName(_fromUtf8("label_oassword"))

        self.retranslateUi(DialogoVerificarAdmin)
        QtCore.QMetaObject.connectSlotsByName(DialogoVerificarAdmin)

    def retranslateUi(self, DialogoVerificarAdmin):
        DialogoVerificarAdmin.setWindowTitle(_translate("DialogoVerificarAdmin", "Verificacion de Usuario", None))
        self.btn_verificar.setText(_translate("DialogoVerificarAdmin", "Verificar", None))
        self.label_usuario.setText(_translate("DialogoVerificarAdmin", "Usuario", None))
        self.label_oassword.setText(_translate("DialogoVerificarAdmin", "Contraseña", None))
