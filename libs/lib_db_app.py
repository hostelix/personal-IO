#! /usr/bin/python

import sqlite3 as dblite
from libs import paths
import os
from lib_extras import encriptar_password


class PersonalIOdb:
    def __init__(self):
        self.conexion = dblite.connect(paths.PATH_DB)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.close()

    def cerrar_cursor(self):
        self.cursor.close()

    def cerrar(self):
        self.cerrar_cursor()
        self.cerrar_conexion()

    def get_data_select(self, nombre_tabla):
        resultado = self.cursor.execute("SELECT descripcion FROM %s" % (nombre_tabla)).fetchall()

        return ["%s" % elemento[0] for elemento in resultado]

    def crear_tablas(self):
        lista_archivos_sql = os.listdir(paths.CARPETA_ARCHIVOS_SQL)

        for archivo in lista_archivos_sql:

            ruta_archivo = os.path.join(paths.CARPETA_ARCHIVOS_SQL, archivo)
            sql = open(ruta_archivo).read()
            try:
                self.cursor.executescript(sql)

            except dblite.Error, e:
                if self.conexion:
                    self.conexion.rollback()

                print "Error %s:" % e.args[0]

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
                VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, %d );""" % (
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

    def registrar_administrador(self, datos):

        try:
            self.cursor.execute("""
                INSERT INTO administradores (
                    usuario,
                    email,
                    password
                )
                VALUES ( :usuario, :email, :password);""", datos)

            print self.conexion.commit()
        except dblite.Error, e:
            if self.conexion:
                self.conexion.rollback()

            print "Error %s:" % e.args[0]

    def autenticar_administrador(self, datos):
        try:
            self.cursor.execute("""
               SELECT count(*) FROM administradores
               WHERE usuario = '%s' AND password = '%s' LIMIT 1""" % (
            datos['usuario'], encriptar_password(datos['password'])))

            resultado = self.cursor.fetchone()

            return bool(resultado[0])

        except dblite.Error, e:
            if self.conexion:
                self.conexion.rollback()

            print "Error %s:" % e.args[0]
