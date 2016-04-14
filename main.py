#! /usr/bin/python
import sys
from interfaces.dialogo_registro_datos import *
from interfaces.pantalla_principal import *


class VentanaPrincipal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.action_salir, QtCore.SIGNAL("triggered()"), self.salir_app)
        QtCore.QObject.connect(self.ui.action_registrar_personal, QtCore.SIGNAL("triggered()"),
                               self.abrir_dialogo_registro_personal)

    def salir_app(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Mensaje de alerta")
        msgBox.setText("Se va a cerrar la aplicacion")
        msgBox.exec_()
        exit()

    def abrir_dialogo_registro_personal(self):
        Registro_personal = DialogoRegistroDatos().exec_()


class DialogoRegistroDatos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogoRegistroDatos()
        self.ui.setupUi(self)

        # QtCore.QObject.connect(self.ui.action_salir, QtCore.SIGNAL("triggered()"),self.cerrar_dialogo)

    def cerrar_dialogo(self):
        exit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = VentanaPrincipal()

    main.show()

    sys.exit(app.exec_())
