#! /usr/bin/python

from os import path

NOMBRE_DB_APP = "personal_io.db"

NOMBRE_ARCHIVO_CONFIG = "personal_io.conf"

CARPETA_PERSONAL_USER = path.expanduser("~")

CARPETA_APP = ".personal_io"

PATH_CARPETA_APP = path.join(CARPETA_PERSONAL_USER, CARPETA_APP)

PATH_DB = path.join(PATH_CARPETA_APP, NOMBRE_DB_APP)

PATH_ARCHIVO_CONFIG = path.join(PATH_CARPETA_APP, NOMBRE_ARCHIVO_CONFIG)
