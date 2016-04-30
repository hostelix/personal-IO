# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillas_interfaces/interfaz_frame_ver_registros.ui'
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


class Ui_FrameVerRegistros(object):
    def setupUi(self, FrameVerRegistros):
        FrameVerRegistros.setObjectName(_fromUtf8("FrameVerRegistros"))
        FrameVerRegistros.resize(648, 449)
        FrameVerRegistros.setFrameShape(QtGui.QFrame.StyledPanel)
        FrameVerRegistros.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayoutWidget = QtGui.QWidget(FrameVerRegistros)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 631, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontal_layout1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout1.setObjectName(_fromUtf8("horizontal_layout1"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontal_layout1.addWidget(self.label_2)
        self.input_busqueda = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.input_busqueda.setObjectName(_fromUtf8("input_busqueda"))
        self.horizontal_layout1.addWidget(self.input_busqueda)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontal_layout1.addItem(spacerItem)
        self.label_parametros = QtGui.QLabel(FrameVerRegistros)
        self.label_parametros.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.label_parametros.setObjectName(_fromUtf8("label_parametros"))
        self.verticalLayoutWidget = QtGui.QWidget(FrameVerRegistros)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 631, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla_resultados = QtGui.QTableView(self.verticalLayoutWidget)
        self.tabla_resultados.setObjectName(_fromUtf8("tabla_resultados"))
        self.verticalLayout.addWidget(self.tabla_resultados)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(FrameVerRegistros)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 421, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontal_layout2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontal_layout2.setObjectName(_fromUtf8("horizontal_layout2"))
        self.label_fecha = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_fecha.setObjectName(_fromUtf8("label_fecha"))
        self.horizontal_layout2.addWidget(self.label_fecha)
        self.select_dia = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.select_dia.setObjectName(_fromUtf8("select_dia"))
        self.horizontal_layout2.addWidget(self.select_dia)
        self.select_mes = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.select_mes.setObjectName(_fromUtf8("select_mes"))
        self.horizontal_layout2.addWidget(self.select_mes)
        self.select_ano = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.select_ano.setObjectName(_fromUtf8("select_ano"))
        self.horizontal_layout2.addWidget(self.select_ano)

        self.retranslateUi(FrameVerRegistros)
        QtCore.QMetaObject.connectSlotsByName(FrameVerRegistros)

    def retranslateUi(self, FrameVerRegistros):
        FrameVerRegistros.setWindowTitle(_translate("FrameVerRegistros", "Frame", None))
        self.label_2.setText(_translate("FrameVerRegistros", "Escribar el nombre del empleado que desa buscar:", None))
        self.label_parametros.setText(_translate("FrameVerRegistros", "Parametros de Busqueda", None))
        self.label_fecha.setText(_translate("FrameVerRegistros", "Buscar por fecha:", None))
