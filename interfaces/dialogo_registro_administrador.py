# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_registro_administrador.ui'
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

class Ui_DialogoRegistroDatosAdministrador(object):
    def setupUi(self, DialogoRegistroDatosAdministrador):
        DialogoRegistroDatosAdministrador.setObjectName(_fromUtf8("DialogoRegistroDatosAdministrador"))
        DialogoRegistroDatosAdministrador.resize(586, 368)
        self.groupBox = QtGui.QGroupBox(DialogoRegistroDatosAdministrador)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 541, 291))
        self.groupBox.setStyleSheet(_fromUtf8("font-size:18px;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.input_usuario = QtGui.QLineEdit(self.groupBox)
        self.input_usuario.setGeometry(QtCore.QRect(0, 100, 241, 31))
        self.input_usuario.setStyleSheet(_fromUtf8("background-color: white;"))
        self.input_usuario.setObjectName(_fromUtf8("input_usuario"))
        self.input_email = QtGui.QLineEdit(self.groupBox)
        self.input_email.setGeometry(QtCore.QRect(280, 100, 241, 31))
        self.input_email.setStyleSheet(_fromUtf8("background-color: white;"))
        self.input_email.setObjectName(_fromUtf8("input_email"))
        self.input_password = QtGui.QLineEdit(self.groupBox)
        self.input_password.setGeometry(QtCore.QRect(0, 200, 241, 31))
        self.input_password.setStyleSheet(_fromUtf8("background-color: white;"))
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.label_usuario = QtGui.QLabel(self.groupBox)
        self.label_usuario.setGeometry(QtCore.QRect(0, 70, 71, 21))
        self.label_usuario.setStyleSheet(_fromUtf8("font-size: 18px;"))
        self.label_usuario.setObjectName(_fromUtf8("label_usuario"))
        self.label_email = QtGui.QLabel(self.groupBox)
        self.label_email.setGeometry(QtCore.QRect(280, 70, 59, 17))
        self.label_email.setObjectName(_fromUtf8("label_email"))
        self.label_password = QtGui.QLabel(self.groupBox)
        self.label_password.setGeometry(QtCore.QRect(0, 170, 101, 17))
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.input_repassword = QtGui.QLineEdit(self.groupBox)
        self.input_repassword.setGeometry(QtCore.QRect(280, 200, 241, 31))
        self.input_repassword.setStyleSheet(_fromUtf8("background-color: white;"))
        self.input_repassword.setObjectName(_fromUtf8("input_repassword"))
        self.label_repassword = QtGui.QLabel(self.groupBox)
        self.label_repassword.setGeometry(QtCore.QRect(280, 170, 171, 17))
        self.label_repassword.setObjectName(_fromUtf8("label_repassword"))
        self.btn_cerrar = QtGui.QPushButton(DialogoRegistroDatosAdministrador)
        self.btn_cerrar.setGeometry(QtCore.QRect(350, 300, 91, 31))
        self.btn_cerrar.setStyleSheet(_fromUtf8(""))
        self.btn_cerrar.setObjectName(_fromUtf8("btn_cerrar"))
        self.btn_registrar = QtGui.QPushButton(DialogoRegistroDatosAdministrador)
        self.btn_registrar.setGeometry(QtCore.QRect(450, 300, 101, 31))
        self.btn_registrar.setObjectName(_fromUtf8("btn_registrar"))

        self.retranslateUi(DialogoRegistroDatosAdministrador)
        QtCore.QMetaObject.connectSlotsByName(DialogoRegistroDatosAdministrador)

    def retranslateUi(self, DialogoRegistroDatosAdministrador):
        DialogoRegistroDatosAdministrador.setWindowTitle(
            _translate("DialogoRegistroDatosAdministrador", "Registro Administrador", None))
        self.groupBox.setTitle(_translate("DialogoRegistroDatosAdministrador", "Datos del Administrador", None))
        self.label_usuario.setText(_translate("DialogoRegistroDatosAdministrador", "Usuario", None))
        self.label_email.setText(_translate("DialogoRegistroDatosAdministrador", "Email", None))
        self.label_password.setText(_translate("DialogoRegistroDatosAdministrador", "Contraseña", None))
        self.label_repassword.setText(_translate("DialogoRegistroDatosAdministrador", "Confirmar contraseña", None))
        self.btn_cerrar.setText(_translate("DialogoRegistroDatosAdministrador", "Cerrar", None))
        self.btn_registrar.setText(_translate("DialogoRegistroDatosAdministrador", "Registrar", None))
