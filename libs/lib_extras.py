from libs import paths
from interfaces.dialogo_verificar_usuario import *
from hashlib import md5
from datetime import datetime


def confirmar_salida_app(_self):
    respuesta = QtGui.QMessageBox.question(_self, 'Confirmar la salida',
                                           "Esta seguro que desea cerrar la aplicacion?",
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

    return respuesta == QtGui.QMessageBox.Yes


def validar_campos_vacios(diccionario_datos, lista_keys):
    for key in lista_keys:
        if type(diccionario_datos[key]) == str:
            if len(diccionario_datos[key].strip()) == 0:
                return False

    return True


def obtener_hora(separador):
    hora = str(datetime.now().hour)
    minuto = str(datetime.now().minute)
    segundo = str(datetime.now().second)

    return "%s{0}%s{0}%s".format(separador) % (hora, minuto, segundo)

def saludo_dia_noche():
    hora = datetime.now().hour

    if (hora >= 4 and hora < 12):
        return "Buenos Dias"
    elif (hora >= 12 and hora <= 17):
        return "Buenas Tardes"
    else:
        return "Buenas Noches"


def encriptar_password(string_password):
    tmp = md5()
    tmp.update(string_password.encode('UTF-8'))
    return tmp.hexdigest()


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

        self.ui.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.input_usuario.setFocus()

        QtCore.QObject.connect(self.ui.btn_verificar, QtCore.SIGNAL("clicked()"),
                               self.verificar_credenciales)

    def verificar_credenciales(self):
        datos = {
            'usuario': str(self.ui.input_usuario.text()),
            'password': str(self.ui.input_password.text()),
        }

        existe_admin = self.personal_io_db.autenticar_administrador(datos)

        if existe_admin:
            print("Acceso concedido")
            self.close()
            return True
        else:
            print ("Acceso denegado")
            return False
