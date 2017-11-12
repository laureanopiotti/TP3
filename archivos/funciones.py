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
		return linea_a_devolver
	except IOError:
		return 'Problema con el archivo'

def interpreto_archivo(archivo):
	"""..."""

	archivo_limpio = leer_archivo(archivo)

	return interpretar_valores(archivo_limpio)


def interpretar_valores(archivo_limpio):
	"""..."""

	cola = Cola()
	cola.encolar(0)
	cola_aux = Cola()
	pila1 = Pila()
	pila2 = Pila()

	for char in archivo_limpio:
		#print(cola.ver_primero())
		if char == '!':
			cola.encolar(0)

		elif char == '=':
			cola.encolar(cola.desencolar())

		elif char == '-':
			cola = _adm(cola,'-')

		elif char == '_':
			cola = _adm(cola,'+')

		elif char == '\\':
			e = cola.ver_primero()

		elif char == '*':
			e = cola.desencolar()
			print(chr(e),end='')
			cola.encolar(e)

	return cola
def _adm(cola,signo):
	"""..."""
	#print("COLA PRINCIPAL",cola)
	cola_aux = Cola()
	e = cola.desencolar()
	while not cola.esta_vacia():
		cola_aux.encolar(cola.desencolar())
	#print("COLA AUX",cola_aux)
	if signo == '+':
		cola.encolar(e+1)
	else:
		cola.encolar(e-1)
	while not cola_aux.esta_vacia():
		cola.encolar(cola_aux.desencolar())

	return cola 












