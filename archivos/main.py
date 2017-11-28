import argparse
import os
from Interprete import Interprete

def main():
	"""Funcion principal que llamara a Interprete para ejecutar el archivo SCEQL
	Recibe como argumento el archivo ingresado por el usuario por consola."""
	parser = argparse.ArgumentParser(description='Interprete de codigo SCEQL')
	parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
	parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
	args = parser.parse_args()

	nombre_archivo = args.archivo
	modo_debug = args.debug

	extension = nombre_archivo.split(".")[1]

	if os.path.isfile(nombre_archivo) and extension == "sceql":
		interprete = Interprete()
		interprete.leer_archivo(nombre_archivo)
		interprete.interpretar_valores(modo_debug)

	else:
		print("El archivo ingresado es incorrecto, por favor ingrese un archivo correcto.")

main()