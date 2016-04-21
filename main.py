#! /usr/bin/python
import sys

from interfaces.dialogo_registro_datos import *
from interfaces.pantalla_principal import *
from interfaces.dialogo_registro_administrador import *
from libs.lib_db_app import PersonalIOdb
from libs.lib_extras import *
from libs.paths import *


class VentanaPrincipal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        # Variable para manejar la base de datos
        self.personal_io_db = PersonalIOdb()

        # Seteamos el icono de la aplicacion
        setear_icono_app(self)

        # Conexion de acciones con las senales
        QtCore.QObject.connect(self.ui.action_salir, QtCore.SIGNAL("triggered()"), self.salir_app)
        QtCore.QObject.connect(self.ui.action_registrar_personal, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_personal)
        QtCore.QObject.connect(self.ui.action_registrar_adminitrador, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_administrador)

    def salir_app(self):
        if confirmar_salida_app(self):
            self.personal_io_db.cerrar()
            exit()

    def abrir_dialogo_registro_personal(self):
        if verificar_is_admin(self.personal_io_db):
            DialogoRegistroDatos(self.personal_io_db).exec_()

    def abrir_dialogo_registro_administrador(self):
        if verificar_is_admin(self.personal_io_db):
            DialogoRegistroDatosAdministrador(self.personal_io_db).exec_()

    def centrar_ventana(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


class DialogoRegistroDatos(QtGui.QDialog):
    def __init__(self, base_de_datos, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoRegistroDatos()
        self.ui.setupUi(self)

        self.personal_io_db = base_de_datos

        # Seteamos el icono de la aplicacion
        setear_icono_app(self)

        # Limpiamos los selects
        self.ui.select_nivel_instruccion.clear()
        self.ui.select_cargos.clear()

        # Cargamos los datos en los selects

        self.ui.select_nivel_instruccion.addItems(self.personal_io_db.get_data_select('niveles_instruccion'))
        self.ui.select_cargos.addItems(self.personal_io_db.get_data_select('cargos'))

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
            'email': str(self.ui.input_email.text()),
            'id_nivel_instruccion': int(self.ui.select_nivel_instruccion.currentIndex() + 1),
            'id_cargo': int(self.ui.select_cargos.currentIndex() + 1),
            'id_sexo': int(self.ui.select_sexo.currentIndex() + 1)
        }

        print datos

        self.personal_io_db.registrar_persona(datos)

    def cerrar_dialogo(self):
        self.close()


class DialogoRegistroDatosAdministrador(QtGui.QDialog):
    def __init__(self, base_de_datos, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoRegistroDatosAdministrador()
        self.ui.setupUi(self)

        # Seteamos el icono de la aplicacion
        setear_icono_app(self)

        self.personal_io_db = base_de_datos

        # Conectamos los botones con sus funciones para realizar acciones
        QtCore.QObject.connect(self.ui.btn_cerrar, QtCore.SIGNAL("clicked()"), self.cerrar_dialogo)
        QtCore.QObject.connect(self.ui.btn_registrar, QtCore.SIGNAL("clicked()"), self.procesar_registro)

    def procesar_registro(self):
        datos = {
        }

        print datos

        self.personal_io_db.registrar_persona(datos)

    def cerrar_dialogo(self):
        self.close()


if __name__ == '__main__':
    aplicacion = QtGui.QApplication(sys.argv)

    # Para traducir los textos default en la libreria al lenguaje del equipo
    traducir_aplicacion(aplicacion)

    ventana_main = VentanaPrincipal()

    ventana_main.centrar_ventana()
    ventana_main.show()

    sys.exit(aplicacion.exec_())
