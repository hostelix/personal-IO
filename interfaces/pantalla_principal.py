# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_pantalla_principal.ui'
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

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName(_fromUtf8("VentanaPrincipal"))
        VentanaPrincipal.resize(640, 480)
        self.centralwidget = QtGui.QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_salir = QtGui.QMenu(self.menubar)
        self.menu_salir.setObjectName(_fromUtf8("menu_salir"))
        self.menu_registro = QtGui.QMenu(self.menubar)
        self.menu_registro.setObjectName(_fromUtf8("menu_registro"))
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        VentanaPrincipal.setStatusBar(self.statusbar)
        self.action_salir = QtGui.QAction(VentanaPrincipal)
        self.action_salir.setObjectName(_fromUtf8("action_salir"))
        self.action_registrar_personal = QtGui.QAction(VentanaPrincipal)
        self.action_registrar_personal.setObjectName(_fromUtf8("action_registrar_personal"))
        self.action_registrar_adminitrador = QtGui.QAction(VentanaPrincipal)
        self.action_registrar_adminitrador.setObjectName(_fromUtf8("action_registrar_adminitrador"))
        self.menu_salir.addAction(self.action_salir)
        self.menu_registro.addAction(self.action_registrar_personal)
        self.menu_registro.addAction(self.action_registrar_adminitrador)
        self.menubar.addAction(self.menu_salir.menuAction())
        self.menubar.addAction(self.menu_registro.menuAction())

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Control Asistencia", None))
        self.menu_salir.setTitle(_translate("VentanaPrincipal", "&Archivo", None))
        self.menu_registro.setTitle(_translate("VentanaPrincipal", "&Registro", None))
        self.action_salir.setText(_translate("VentanaPrincipal", "&Salir", None))
        self.action_registrar_personal.setText(_translate("VentanaPrincipal", "&Registrar Personal", None))
        self.action_registrar_adminitrador.setText(_translate("VentanaPrincipal", "&Registrar Adminitrador", None))

