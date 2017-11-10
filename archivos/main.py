import argparse

def main():
	"""..."""
	parser = argparse.ArgumentParser(description='Interprete de codigo SCEQL')
	parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
	parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
	args = parser.parse_args()

	nombre_archivo = args.archivo
	modo_debug = args.debug
	print(nombre_archivo, modo_debug, sep="||")

	"""Codigo"""

main()