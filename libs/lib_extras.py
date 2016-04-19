from PyQt4 import QtGui, QtCore
from libs import paths

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
