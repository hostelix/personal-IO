from libs import paths
from interfaces.dialogo_verificar_usuario import *


def confirmar_salida_app(_self):
    respuesta = QtGui.QMessageBox.question(_self, 'Confirmar la salida',
                                           "Esta seguro que desea cerrar la aplicacion?",
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

    return respuesta == QtGui.QMessageBox.Yes


def setear_icono_app(_self):
    _self.setWindowIcon(QtGui.QIcon(paths.PATH_ICON_APP_64X64))


def guardar_configuracion(self):
    settings = QtCore.QSettings(paths.PATH_ARCHIVO_CONFIG, QtCore.QSettings.NativeFormat)
    settings.setValue('text', 'algo')


def traducir_aplicacion(_aplicacion):
    translator = QtCore.QTranslator(_aplicacion)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    _aplicacion.installTranslator(translator)


def verificar_is_admin(base_datos):
    dialogo = DialogoVerificarUsuario(base_datos)
    dialogo.exec_()
    return dialogo.verificar_credenciales()


class DialogoVerificarUsuario(QtGui.QDialog):
    def __init__(self, base_de_datos, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoVerificarAdmin()
        self.ui.setupUi(self)
        # Seteamos el icono de la aplicacion
        setear_icono_app(self)

        self.personal_io_db = base_de_datos

        QtCore.QObject.connect(self.ui.btn_verificar, QtCore.SIGNAL("clicked()"),
                               self.verificar_credenciales)

    def verificar_credenciales(self):
        datos = {
            'usuario': str(self.ui.input_usuario.text()),
            'password': str(self.ui.input_password.text()),
        }

        existe_admin = self.personal_io_db.autenticar_administrador(datos)

        # if 'hostelix' == datos['usuario'] and 'canaima' == datos['password']:
        if existe_admin:
            print "Acceso concedido"
            self.close()
            return True
        else:
            print  "Acceso denegado"
            return False
