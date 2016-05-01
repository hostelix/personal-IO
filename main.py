#! /usr/bin/python
import sys

from interfaces.dialogo_registro_datos import *
from interfaces.pantalla_principal import *
from interfaces.dialogo_registro_administrador import *
from interfaces.dialogo_verificar_cedula import *
from interfaces.frame_ver_registros import *
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

        # self.personal_io_db.crear_tablas()

        # Conexion de acciones con las senales
        QtCore.QObject.connect(self.ui.action_salir, QtCore.SIGNAL("triggered()"), self.salir_app)
        QtCore.QObject.connect(self.ui.action_registrar_personal, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_personal)
        QtCore.QObject.connect(self.ui.action_registrar_adminitrador, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_administrador)
        QtCore.QObject.connect(self.ui.action_verificacion_cedula, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_verificacion_cedula)
        QtCore.QObject.connect(self.ui.action_ver_registros_asistencia, QtCore.SIGNAL("triggered()"),
                               self.cargar_frame_ver_registros_asistencia)

        self.setCentralWidget(FrameImagenPrincipal(self))

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

    def abrir_dialogo_verificacion_cedula(self):
        DialogoVerificarCedula(self.personal_io_db).exec_()

    def cargar_frame_ver_registros_asistencia(self):
        if verificar_is_admin(self.personal_io_db):
            frame_registros_asistencia = FrameVerRegistros(self.personal_io_db)

            self.setCentralWidget(frame_registros_asistencia)


    def centrar_ventana(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


class FrameImagenPrincipal(QtGui.QWidget):
    def __init__(self, parent):
        super(FrameImagenPrincipal, self).__init__(parent)

        contenedor_img = QtGui.QLabel(self)
        contenedor_img.setGeometry(250, 1, 380, 400)
        pixmap = QtGui.QPixmap('/home/hostelix/Escritorio/logo_simon_bolivar.png')
        pixmap = pixmap.scaledToHeight(160)
        pixmap = pixmap.scaledToWidth(160)
        contenedor_img.setPixmap(pixmap)


class FrameVerRegistros(QtGui.QWidget):
    def __init__(self, base_de_datos, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_FrameVerRegistros()
        self.ui.setupUi(self)

        self.personal_io_db = base_de_datos

        self.ui.select_dia.addItems([''] + ['%d' % dia for dia in range(1, 32)])
        self.ui.select_mes.addItems(('', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                     'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'))
        self.ui.select_ano.addItems([''] + ['%d' % dia for dia in range(2000, 2030)])

        self.cargar_header_tabla()
        self.cargar_datos_tabla(self.personal_io_db.obtener_asistencia())

        self.ui.tabla_resultados.resizeColumnsToContents()

        QtCore.QObject.connect(self.ui.btn_buscar, QtCore.SIGNAL("clicked()"),
                               self.cargar_datos_busqueda)

    def cargar_header_tabla(self):
        cabeceras = ['Nombre Completo', 'Cedula', 'Cargo', 'Hora entrada', 'Hora Salida', 'Fecha']

        # Seteamos el numero de columnas que tendra la tabla
        self.ui.tabla_resultados.setColumnCount(len(cabeceras))

        for n, elem in enumerate(cabeceras):
            self.ui.tabla_resultados.setHorizontalHeaderItem(n, QtGui.QTableWidgetItem(elem))

    def cargar_datos_tabla(self, _datos):
        datos = _datos

        # Seteamos el numero de filas que obtengamos de la db
        self.ui.tabla_resultados.setRowCount(len(datos))

        for num_fila, fila in enumerate(datos):
            nombre_completo = fila[1].capitalize() + ' ' + fila[2].capitalize()
            fecha = fila[6].split('-')
            fecha = "{0}/{1}/{2}".format(fecha[2], fecha[1], fecha[0])

            self.ui.tabla_resultados.setItem(num_fila, 0, QtGui.QTableWidgetItem(nombre_completo))
            self.ui.tabla_resultados.setItem(num_fila, 1,
                                             QtGui.QTableWidgetItem(fila[0] if fila[0] else "No Especificado"))
            self.ui.tabla_resultados.setItem(num_fila, 2,
                                             QtGui.QTableWidgetItem(fila[3] if fila[3] else "No Especificado"))
            self.ui.tabla_resultados.setItem(num_fila, 3, QtGui.QTableWidgetItem(fila[4] if fila[4] else "Sin Entrada"))
            self.ui.tabla_resultados.setItem(num_fila, 4, QtGui.QTableWidgetItem(fila[5] if fila[5] else "Sin Salida"))
            self.ui.tabla_resultados.setItem(num_fila, 5, QtGui.QTableWidgetItem(fecha if fecha else "No Especificado"))

    def cargar_datos_busqueda(self):
        fecha_busqueda = {
            'dia': str(self.ui.select_dia.currentText()),
            'mes': str(self.ui.select_mes.currentIndex()),
            'ano': str(self.ui.select_ano.currentText()),
        }

        pista_buscar = str(self.ui.input_busqueda.text())

        parametros = {}

        if len(pista_buscar.strip()) != 0:
            parametros['nombre_empleado'] = pista_buscar

        if len(fecha_busqueda['dia'].strip()) != 0:
            parametros['dia'] = fecha_busqueda['dia']

        if fecha_busqueda['mes'].strip() != '0':
            parametros['mes'] = fecha_busqueda['mes']

        if len(fecha_busqueda['ano'].strip()) != 0:
            parametros['ano'] = fecha_busqueda['ano']

        datos = self.personal_io_db.obtener_busqueda_asistencia(parametros)

        self.ui.tabla_resultados.clear()
        self.cargar_header_tabla()
        self.cargar_datos_tabla(datos)

        self.ui.tabla_resultados.resizeColumnsToContents()


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
        self.ui.select_sexo.addItems(('Masculino', 'Femenino'))

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

        if validar_campos_vacios(datos, ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
                                         'cedula']) == False:
            QtGui.QMessageBox.warning(self, "Error en Formulario", "Tienes que llenar todos los campos")
        else:
            registro = self.personal_io_db.registrar_persona(datos)

            if registro:
                QtGui.QMessageBox.information(self, "Registro Personal", "Personal Registrado con exito")
                self.close()
            else:
                QtGui.QMessageBox.critical(self, "Error en Formulario",
                                           "Ha ocurrido un error al registrar el formulario")

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

        self.ui.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.input_repassword.setEchoMode(QtGui.QLineEdit.Password)

        # Conectamos los botones con sus funciones para realizar acciones
        QtCore.QObject.connect(self.ui.btn_cerrar, QtCore.SIGNAL("clicked()"), self.cerrar_dialogo)
        QtCore.QObject.connect(self.ui.btn_registrar, QtCore.SIGNAL("clicked()"), self.procesar_registro)

    def procesar_registro(self):
        datos = {
            'usuario': str(self.ui.input_usuario.text()),
            'email': str(self.ui.input_email.text()),
            'password': str(self.ui.input_password.text()),
            'repassword': str(self.ui.input_repassword.text())
        }

        if validar_campos_vacios(datos, ['usuario', 'email', 'password', 'repassword']) == False:
            QtGui.QMessageBox.warning(self, "Error en Formulario", "Tienes que llenar todos los campos")
        else:
            if (datos['password'] != datos['repassword']):
                QtGui.QMessageBox.warning(self, "Error en Formulario", "Las contrasenas no coinciden")
            else:
                datos['password'] = encriptar_password(datos['password'])
                registro = self.personal_io_db.registrar_administrador(datos)

                if registro:
                    QtGui.QMessageBox.information(self, "Registro Administrador", "Administrador creado con exito")
                    self.close()
                else:
                    QtGui.QMessageBox.critical(self, "Error en Formulario",
                                               "Ha ocurrido un error al registrar el administrador")

    def cerrar_dialogo(self):
        self.close()


class DialogoVerificarCedula(QtGui.QDialog):
    def __init__(self, base_de_datos, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoVerificarCedula()
        self.ui.setupUi(self)

        self.personal_io_db = base_de_datos

        # Seteamos el icono de la aplicacion
        setear_icono_app(self)

        self.ui.input_cedula.setFocus()

        # Conectamos los botones con sus funciones para realizar acciones
        QtCore.QObject.connect(self.ui.btn_aceptar, QtCore.SIGNAL("clicked()"), self.procesar_accion)

    def procesar_accion(self):
        datos = {
            'cedula': str(self.ui.input_cedula.text())
        }
        if validar_campos_vacios(datos, ['cedula']) == False:
            QtGui.QMessageBox.warning(self, "Error en Formulario", "El campo no puede quedar vacio")
        else:
            tamano_input = len(datos['cedula'])
            if (tamano_input >= 6 and tamano_input <= 8) and datos['cedula'].isdigit():
                datos_empleado = self.personal_io_db.buscar_personal(datos)
                if datos_empleado:
                    nombre_completo = "%s %s" % (datos_empleado[1].capitalize(), datos_empleado[2].capitalize())

                    respuesta = self.personal_io_db.proceso_entrada_salida(datos)

                    if respuesta['tipo'] == "completo":
                        QtGui.QMessageBox.warning(self, "Atencion!",
                                                  "Ya ha terminado su Turno de trabajo por el dia de hoy")
                        self.ui.input_cedula.clear()
                        self.close()
                    else:
                        saludo = "%s %s, Hora de %s: %s" % (
                            saludo_dia_noche(), nombre_completo, respuesta['tipo'], respuesta['hora'])

                        QtGui.QMessageBox.information(self, "Bienvenido", saludo)
                        self.ui.input_cedula.clear()
                        self.close()
                else:
                    QtGui.QMessageBox.warning(self, "Ha ocurrido un problema",
                                              "Error! La cedula no existe en la base de datos")
            else:
                QtGui.QMessageBox.warning(self, "Error en Formulario", "La cedula introducida es incorrecta")
            """registro = self.personal_io_db.registrar_persona(datos)

            if registro:
                QtGui.QMessageBox.information(self, "Registro Personal", "Personal Registrado con exito")
                self.close()
            else:
                QtGui.QMessageBox.critical(self, "Error en Formulario",
                                           "Ha ocurrido un error al registrar el formulario")"""


if __name__ == '__main__':
    aplicacion = QtGui.QApplication(sys.argv)

    # Para traducir los textos default en la libreria al lenguaje del equipo
    traducir_aplicacion(aplicacion)

    ventana_main = VentanaPrincipal()

    ventana_main.centrar_ventana()
    ventana_main.show()

    sys.exit(aplicacion.exec_())
