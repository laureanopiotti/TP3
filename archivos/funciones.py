from Pila import Pila
from Cola import Cola
#Funciones

def leer_archivo(archivo):
	"""Recibe un archivo de tipo sceql y lo recorre caracter por caracter filtrando por los comandos validos del lenguaje SCEQL"""
	try:
		with open(archivo) as archivo_a_recorrer:
			linea_a_devolver = ""
			sceql_comandos = dict.fromkeys(['!','=','-','_','/','\\','*'])
			for linea in archivo_a_recorrer:
				linea = linea.rstrip('/n').replace(' ','')
				for char in linea:
					if char in sceql_comandos:
						linea_a_devolver += char
			print(linea_a_devolver)
	except IOError:
		return 'Problema con el archivo'

def interpreto_archivo(archivo):
	"""..."""

	linea_a_recorrer = leer_archivo(archivo)
	