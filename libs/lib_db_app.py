#! /usr/bin/python

import sqlite3 as dblite
from libs import paths
import os
from .lib_extras import encriptar_password, obtener_fecha, obtener_hora


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

            except dblite.Error as err:
                if self.conexion:
                    self.conexion.rollback()

                print("Error %s:" % err.args[0])

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
                VALUES ( :primer_nombre, :segundo_nombre, :primer_apellido, :segundo_apellido, :cedula, :email, :id_sexo, :id_cargo, :id_nivel_instruccion);""",
                                datos)

            self.conexion.commit()

            return True

        except dblite.Error as err:
            if self.conexion:
                self.conexion.rollback()

            print("Error %s:" % err.args[0])

            return False

    def registrar_administrador(self, datos):

        try:
            self.cursor.execute("""
                INSERT INTO administradores (
                    usuario,
                    email,
                    password
                )
                VALUES ( :usuario, :email, :password);""", datos)

            self.conexion.commit()

            return True

        except dblite.Error as err:
            if self.conexion:
                self.conexion.rollback()

            print("Error %s:" % err.args[0])

            return False

    def autenticar_administrador(self, datos):
        try:
            self.cursor.execute("""
               SELECT count(*) FROM administradores
               WHERE usuario = '%s' AND password = '%s' LIMIT 1""" % (
                datos['usuario'], encriptar_password(datos['password'])))

            resultado = self.cursor.fetchone()

            return bool(resultado[0])

        except dblite.Error as err:
            if self.conexion:
                self.conexion.rollback()

            print("Error %s:" % err.args[0])

    def buscar_personal(self, datos):
        try:
            self.cursor.execute("""
            SELECT
                cedula,
                primer_nombre,
                primer_apellido
            FROM personal
            WHERE cedula = :cedula """, datos)

        except dblite.Error as err:
            if self.conexion:
                self.conexion.rollback()

            print("Error %s:" % err.args[0])

        else:
            return self.cursor.fetchone()

    def proceso_entrada_salida(self, datos):
        datos['fecha'] = obtener_fecha('YYYY-MM-DD')

        retorno = {}

        try:
            self.cursor.execute("""
            SELECT
                id, cedula, hora_entrada, hora_salida
            FROM entradas_salidas
            WHERE cedula = :cedula AND fecha = :fecha """, datos)

            resultado = self.cursor.fetchone()

            if resultado:
                if resultado[2] and resultado[3]:
                    retorno['tipo'] = 'completo'
                elif resultado[2] and resultado[3] == None:

                    datos['hora_salida'] = obtener_hora(separador=':')

                    self.cursor.execute("""
                        UPDATE
                            entradas_salidas
                        SET
                            hora_salida = :hora_salida
                        WHERE cedula = :cedula AND fecha = :fecha ;""", datos)

                    self.conexion.commit()

                    retorno['tipo'] = "salida"
                    retorno['hora'] = datos['hora_salida']

            else:
                datos['hora_entrada'] = obtener_hora(separador=':')

                self.cursor.execute("""
                    INSERT INTO entradas_salidas (
                        cedula,
                        hora_entrada,
                        fecha
                    )
                    VALUES ( :cedula, :hora_entrada, :fecha);""", datos)

                self.conexion.commit()

                retorno['tipo'] = "entrada"
                retorno['hora'] = datos['hora_entrada']

        except dblite.Error as err:
            if self.conexion:
                self.conexion.rollback()

            print("Error %s:" % err.args[0])

        else:
            return retorno
