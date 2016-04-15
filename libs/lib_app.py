#! /usr/bin/python

import sqlite3 as dblite
from os.path import expanduser, join


class App:
    def __init__(self, nombre_db):
        ruta_db = join(expanduser('~'), nombre_db)
        self.conexion = dblite.connect(ruta_db)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

    def get_niveles_instruccion(self):
        resultado = self.cursor.execute("SELECT descripcion FROM niveles_instruccion").fetchall()

        return ["%s" % elemento[0] for elemento in resultado]

    def get_cargos(self):
        resultado = self.cursor.execute("SELECT descripcion FROM cargos").fetchall()

        return ["%s" % elemento[0] for elemento in resultado]
