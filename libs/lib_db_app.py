#! /usr/bin/python

import sqlite3 as dblite
from libs import paths


class DataBaseApp:
    def __init__(self):
        self.conexion = dblite.connect(paths.PATH_DB)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.close()

    def cerrar_cursor(self):
        self.cursor.close()

    def get_data_select(self, nombre_tabla):
        resultado = self.cursor.execute("SELECT descripcion FROM %s" % (nombre_tabla)).fetchall()

        return ["%s" % elemento[0] for elemento in resultado]

    def registrar_persona(self, datos):
        try:
            self.cursor.execute("""
                INSERT INTO personal (
                    primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido,
                    cedula,
                    email,
                    id_sexo,
                    id_cargo,
                    id_nivel_instruccion
                )
                VALUES ( %s, %s, %s, %s, %s, %s, %d, %d, %d );""" % (
                datos['primer_nombre'],
                datos['segundo_nombre'],
                datos['primer_apellido'],
                datos['segundo_apellido'],
                datos['cedula'],
                datos['email'],
                datos['id_sexo'],
                datos['id_cargo'],
                datos['id_nivel_instruccion'])
                                )

        except dblite.Error, e:
            if self.conexion:
                self.conexion.rollback()

            print "Error %s:" % e.args[0]
