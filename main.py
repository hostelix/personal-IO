#! /usr/bin/python
import sys

from interfaces.dialogo_registro_datos import *
from interfaces.pantalla_principal import *
from libs.lib_app import App
from libs.lib_extras import *


class VentanaPrincipal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.action_salir, QtCore.SIGNAL("triggered()"), self.salir_app)
        QtCore.QObject.connect(self.ui.action_registrar_personal, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_personal)

    def salir_app(self):
        if confirmar_salida_app(self):
            exit()

    def abrir_dialogo_registro_personal(self):
        DialogoRegistroDatos().exec_()


class DialogoRegistroDatos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoRegistroDatos()
        self.ui.setupUi(self)

        # Limpiamos los selects
        self.ui.select_nivel_instruccion.clear()
        self.ui.select_cargos.clear()

        # Cargamos los datos en los selects
        # self.ui.select_nivel_instruccion.addItems(niveles)
        # self.ui.select_cargos.addItems(cargos)

        # Conectamos los botones con sus funciones para realizar acciones
        QtCore.QObject.connect(self.ui.btn_cerrar, QtCore.SIGNAL("clicked()"), self.cerrar_dialogo)
        QtCore.QObject.connect(self.ui.btn_registrar, QtCore.SIGNAL("clicked()"), self.procesar_registro)

    def procesar_registro(self):
        datos = {
            'primer_nombre': str(self.ui.input_primer_nombre.text()),
            'segundo_nombre': str(self.ui.input_segundo_nombre.text()),
            'primer_apellido': str(self.ui.input_primer_apellido.text()),
            'segundo_apellido': str(self.ui.input_segundo_apellido.text()),
            'cedula': str(self.ui.input_cedula.text()),
            'email': str(self.ui.input_email.text())
        }

        print datos

    def cerrar_dialogo(self):
        self.close()


if __name__ == '__main__':
    aplicacion = QtGui.QApplication(sys.argv)

    # Para traducir los textos default en la libreria al lenguaje del equipo
    translator = QtCore.QTranslator(aplicacion)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    aplicacion.installTranslator(translator)

    ventana_main = VentanaPrincipal()

    ventana_main.show()

    sys.exit(aplicacion.exec_())
