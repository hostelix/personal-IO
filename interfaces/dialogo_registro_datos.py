# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_registro_datos.ui'
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

class Ui_DialogoRegistroDatos(object):
    def setupUi(self, DialogoRegistroDatos):
        DialogoRegistroDatos.setObjectName(_fromUtf8("DialogoRegistroDatos"))
        DialogoRegistroDatos.resize(677, 405)
        DialogoRegistroDatos.setToolTip(_fromUtf8(""))
        self.grupo_datos_personales = QtGui.QGroupBox(DialogoRegistroDatos)
        self.grupo_datos_personales.setGeometry(QtCore.QRect(9, 9, 666, 201))
        self.grupo_datos_personales.setObjectName(_fromUtf8("grupo_datos_personales"))
        self.input_primer_nombre = QtGui.QLineEdit(self.grupo_datos_personales)
        self.input_primer_nombre.setGeometry(QtCore.QRect(10, 50, 141, 29))
        self.input_primer_nombre.setObjectName(_fromUtf8("input_primer_nombre"))
        self.label_primer_nombre = QtGui.QLabel(self.grupo_datos_personales)
        self.label_primer_nombre.setGeometry(QtCore.QRect(14, 30, 111, 17))
        self.label_primer_nombre.setObjectName(_fromUtf8("label_primer_nombre"))
        self.label_segundo_nombre = QtGui.QLabel(self.grupo_datos_personales)
        self.label_segundo_nombre.setGeometry(QtCore.QRect(170, 30, 111, 17))
        self.label_segundo_nombre.setObjectName(_fromUtf8("label_segundo_nombre"))
        self.input_segundo_nombre = QtGui.QLineEdit(self.grupo_datos_personales)
        self.input_segundo_nombre.setGeometry(QtCore.QRect(170, 50, 141, 29))
        self.input_segundo_nombre.setObjectName(_fromUtf8("input_segundo_nombre"))
        self.input_primer_apellido = QtGui.QLineEdit(self.grupo_datos_personales)
        self.input_primer_apellido.setGeometry(QtCore.QRect(330, 50, 141, 29))
        self.input_primer_apellido.setObjectName(_fromUtf8("input_primer_apellido"))
        self.input_segundo_apellido = QtGui.QLineEdit(self.grupo_datos_personales)
        self.input_segundo_apellido.setGeometry(QtCore.QRect(490, 50, 141, 29))
        self.input_segundo_apellido.setObjectName(_fromUtf8("input_segundo_apellido"))
        self.label_primer_apellido = QtGui.QLabel(self.grupo_datos_personales)
        self.label_primer_apellido.setGeometry(QtCore.QRect(330, 30, 111, 17))
        self.label_primer_apellido.setObjectName(_fromUtf8("label_primer_apellido"))
        self.label_segundo_apellido = QtGui.QLabel(self.grupo_datos_personales)
        self.label_segundo_apellido.setGeometry(QtCore.QRect(490, 30, 111, 17))
        self.label_segundo_apellido.setObjectName(_fromUtf8("label_segundo_apellido"))
        self.input_cedula = QtGui.QLineEdit(self.grupo_datos_personales)
        self.input_cedula.setGeometry(QtCore.QRect(10, 120, 141, 29))
        self.input_cedula.setObjectName(_fromUtf8("input_cedula"))
        self.label_cedula = QtGui.QLabel(self.grupo_datos_personales)
        self.label_cedula.setGeometry(QtCore.QRect(14, 100, 111, 17))
        self.label_cedula.setObjectName(_fromUtf8("label_cedula"))
        self.select_sexo = QtGui.QComboBox(self.grupo_datos_personales)
        self.select_sexo.setGeometry(QtCore.QRect(170, 119, 131, 31))
        self.select_sexo.setObjectName(_fromUtf8("select_sexo"))
        self.select_sexo.addItem(_fromUtf8(""))
        self.select_sexo.addItem(_fromUtf8(""))
        self.label_sexo = QtGui.QLabel(self.grupo_datos_personales)
        self.label_sexo.setGeometry(QtCore.QRect(170, 100, 111, 17))
        self.label_sexo.setObjectName(_fromUtf8("label_sexo"))
        self.line = QtGui.QFrame(self.grupo_datos_personales)
        self.line.setGeometry(QtCore.QRect(7, 170, 641, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.acciones_registro = QtGui.QDialogButtonBox(DialogoRegistroDatos)
        self.acciones_registro.setGeometry(QtCore.QRect(440, 340, 201, 51))
        self.acciones_registro.setOrientation(QtCore.Qt.Horizontal)
        self.acciones_registro.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.acciones_registro.setObjectName(_fromUtf8("acciones_registro"))
        self.gurpo_datos_extras = QtGui.QGroupBox(DialogoRegistroDatos)
        self.gurpo_datos_extras.setGeometry(QtCore.QRect(10, 210, 631, 121))
        self.gurpo_datos_extras.setObjectName(_fromUtf8("gurpo_datos_extras"))
        self.input_email = QtGui.QLineEdit(self.gurpo_datos_extras)
        self.input_email.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.input_email.setObjectName(_fromUtf8("input_email"))
        self.label_email = QtGui.QLabel(self.gurpo_datos_extras)
        self.label_email.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.label_email.setObjectName(_fromUtf8("label_email"))
        self.label_cargo = QtGui.QLabel(self.gurpo_datos_extras)
        self.label_cargo.setGeometry(QtCore.QRect(380, 29, 59, 17))
        self.label_cargo.setObjectName(_fromUtf8("label_cargo"))
        self.select_cargos = QtGui.QComboBox(self.gurpo_datos_extras)
        self.select_cargos.setGeometry(QtCore.QRect(380, 50, 181, 31))
        self.select_cargos.setObjectName(_fromUtf8("select_cargos"))
        self.select_nivel_instruccion = QtGui.QComboBox(self.gurpo_datos_extras)
        self.select_nivel_instruccion.setGeometry(QtCore.QRect(180, 50, 181, 31))
        self.select_nivel_instruccion.setObjectName(_fromUtf8("select_nivel_instruccion"))
        self.label_nivel_instruccion = QtGui.QLabel(self.gurpo_datos_extras)
        self.label_nivel_instruccion.setGeometry(QtCore.QRect(180, 30, 131, 17))
        self.label_nivel_instruccion.setObjectName(_fromUtf8("label_nivel_instruccion"))

        self.retranslateUi(DialogoRegistroDatos)
        QtCore.QObject.connect(self.acciones_registro, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogoRegistroDatos.accept)
        QtCore.QObject.connect(self.acciones_registro, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogoRegistroDatos.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogoRegistroDatos)

    def retranslateUi(self, DialogoRegistroDatos):
        DialogoRegistroDatos.setWindowTitle(_translate("DialogoRegistroDatos", "Formulario de Registro", None))
        self.grupo_datos_personales.setTitle(_translate("DialogoRegistroDatos", "Datos Personales", None))
        self.label_primer_nombre.setText(_translate("DialogoRegistroDatos", "Primer Nombre", None))
        self.label_segundo_nombre.setText(_translate("DialogoRegistroDatos", "Segundo Nombre", None))
        self.label_primer_apellido.setText(_translate("DialogoRegistroDatos", "Primer Apellido", None))
        self.label_segundo_apellido.setText(_translate("DialogoRegistroDatos", "Segundo Apellido", None))
        self.label_cedula.setText(_translate("DialogoRegistroDatos", "Cedula", None))
        self.select_sexo.setItemText(0, _translate("DialogoRegistroDatos", "Masculino", None))
        self.select_sexo.setItemText(1, _translate("DialogoRegistroDatos", "Femenino", None))
        self.label_sexo.setText(_translate("DialogoRegistroDatos", "Sexo", None))
        self.gurpo_datos_extras.setTitle(_translate("DialogoRegistroDatos", "Datos Extra", None))
        self.label_email.setText(_translate("DialogoRegistroDatos", "Correo Electronico", None))
        self.label_cargo.setText(_translate("DialogoRegistroDatos", "Cargo", None))
        self.label_nivel_instruccion.setText(_translate("DialogoRegistroDatos", "Nivel de Instruccion", None))

