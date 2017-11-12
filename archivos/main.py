import argparse
from funciones import interpreto_archivo
import os

def main():
	"""..."""
	parser = argparse.ArgumentParser(description='Interprete de codigo SCEQL')
	parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
	parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
	args = parser.parse_args()

	nombre_archivo = args.archivo
	modo_debug = args.debug
	print(nombre_archivo, modo_debug, sep="||")

	extension = nombre_archivo.split(".")[1]

	if os.path.isfile(nombre_archivo) and extension == "sceql":
		if not modo_debug:
			print("Modo normal.")
			interpreto_archivo(nombre_archivo)
		else:
			print("Modo debug.")
	else:
		print("El archivo ingresado es incorrecto, por favor ingrese un archivo correcto.")

main()