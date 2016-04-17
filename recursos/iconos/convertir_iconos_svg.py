import os
import subprocess
import threading

CARPETA_ICONOS_SVG = "svg"

class HiloConvertirIcono(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)
        self.lista_iconos_svg = kwargs["lista_iconos"]
        self.nombre_carpeta = kwargs["nombre_carpeta"]
        self.tamano_icono = kwargs["tamano_icono"]
        
    def run(self):

    	for icono_svg in self.lista_iconos_svg:
		
			path_icono_origen = os.path.join(CARPETA_ICONOS_SVG,icono_svg)
			
			nombre_icono_destino = icono_svg.split('.')[0]
			path_icono_destino = os.path.join(self.nombre_carpeta,nombre_icono_destino)

			comando = "inkscape -z -e {0}.png -w {1} -h {1} {2}".format(path_icono_destino,self.tamano_icono,path_icono_origen)

			lista_comando = comando.split(" ")
			
			subprocess.call(lista_comando)


lista_tamanos = ['16','32','64']

lista_iconos_svg = os.listdir(CARPETA_ICONOS_SVG)

for tamano_icono in lista_tamanos:
	
	nombre_carpeta = "{0}x{0}".format(tamano_icono)
	
	if not os.path.exists(nombre_carpeta):
		os.makedirs(nombre_carpeta)

	hilo = HiloConvertirIcono(lista_iconos=lista_iconos_svg,nombre_carpeta=nombre_carpeta,tamano_icono=tamano_icono)
	hilo.start()

