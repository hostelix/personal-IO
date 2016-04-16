#! /usr/bin/python

from os import path

NOMBRE_DB_APP = "personal_io.db"

NOMBRE_ARCHIVO_CONFIG = "personal_io.conf"

CARPETA_PERSONAL_USER = path.expanduser("~")

CARPETA_APP = ".personal_io"

PATH_CARPETA_APP = path.join(CARPETA_PERSONAL_USER, CARPETA_APP)

PATH_DB = path.join(PATH_CARPETA_APP, NOMBRE_DB_APP)

PATH_ARCHIVO_CONFIG = path.join(PATH_CARPETA_APP, NOMBRE_ARCHIVO_CONFIG)

PATH_ICON_APP_16X16 = path.join('iconos', 'personal_io_16x16.png')
PATH_ICON_APP_32X32 = path.join('iconos', 'personal_io_32x32.png')
PATH_ICON_APP_64X64 = path.join('iconos', 'personal_io_64x64.png')
PATH_ICON_APP_128X128 = path.join('iconos', 'personal_io_128x128.png')
