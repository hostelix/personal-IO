#! /usr/bin/python

from os import path, getcwd

PATH_APP = getcwd()

NOMBRE_DB_APP = "personal_io.db"

NOMBRE_ARCHIVO_CONFIG = "personal_io.conf"

CARPETA_PERSONAL_USER = path.expanduser("~")

CARPETA_APP = ".personal_io"

CARPETA_RECURSOS = path.join(PATH_APP, "recursos")

CARPETA_ICONOS = path.join(CARPETA_RECURSOS, "iconos")

CARPETA_ICONOS_16_x_16 = path.join(CARPETA_ICONOS, "16x16")
CARPETA_ICONOS_32_x_32 = path.join(CARPETA_ICONOS, "32x32")
CARPETA_ICONOS_64_x_64 = path.join(CARPETA_ICONOS, "64x64")

CARPETA_ARCHIVOS_SQL = path.join(PATH_APP, "sql")

PATH_CARPETA_APP = path.join(CARPETA_PERSONAL_USER, CARPETA_APP)

PATH_DB = path.join(PATH_CARPETA_APP, NOMBRE_DB_APP)

PATH_ARCHIVO_CONFIG = path.join(PATH_CARPETA_APP, NOMBRE_ARCHIVO_CONFIG)

PATH_ICON_APP_16X16 = path.join(CARPETA_ICONOS, 'personal_io_16x16.png')
PATH_ICON_APP_32X32 = path.join(CARPETA_ICONOS, 'personal_io_32x32.png')
PATH_ICON_APP_64X64 = path.join(CARPETA_ICONOS, 'personal_io_64x64.png')
PATH_ICON_APP_128X128 = path.join(CARPETA_ICONOS, 'personal_io_128x128.png')
