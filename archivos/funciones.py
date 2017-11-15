from Pila import Pila
from Cola import Cola
from ListaEnlazada import ListaEnlazada
#Funciones

def leer_archivo(archivo):
	"""Recibe un archivo de tipo sceql y lo recorre caracter por caracter filtrando por los comandos validos del lenguaje SCEQL"""
	try:
		dic = {}
		lista = []
		index = 0
		cont = 0
		with open(archivo) as archivo_a_recorrer:
			linea_a_devolver = ListaEnlazada()
			sceql_comandos = dict.fromkeys(['!','=','-','_','/','\\','*'])
			for linea in archivo_a_recorrer:
				linea = linea.rstrip('/n').replace(' ','')
				for char in linea:
					if char in sceql_comandos:
						linea_a_devolver.append(char)
		
		#print(len(linea_a_devolver))
		for char in linea_a_devolver:
			if char == '\\':
				cont+=1
				lista.append(index)
			elif char == '/':
				cont+=1
				dic[index] = lista.pop()
			index += 1

		#print(cont)
		if len(lista):
			raise IndexError("Archivo Incorrecto.")
		#print(dic)
		return linea_a_devolver, dic
	except IOError:
		return 'Problema con el archivo'

def interpreto_archivo(archivo):
	"""..."""

	archivo_limpio, dic = leer_archivo(archivo)

	return interpretar_valores(archivo_limpio, dic)


def interpretar_valores(archivo_limpio, dic_recibido):
	"""..."""

	cola = Cola()
	cola.encolar(0)
	cola_aux = Cola()
	pila1 = Pila()
	pila2 = Pila()
	dic_aux = {}

	for clave, valor in dic_recibido.items():
		dic_aux[valor] = clave

	indice = 0
	#print(archivo_limpio.len)
	longitud = archivo_limpio.len()
	while indice != (longitud - 1):
	#for index, char in enumerate(archivo_limpio):
		#print(index, char, cola)
		char = archivo_limpio.jose(indice)
		print("CHAR",char,"COLA",cola,"INDICE",indice)
		#while True:
		#	ingreso = input("Apreta enter:")
		#	break
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
			if e == 0:
				indice = dic_aux[indice] + 1
				continue
				#print("Doble barra", index)

		elif char == '/':
			indice = dic_recibido[indice]
			continue
			#print("Barra Simple", index)

		elif char == '*':
			e = cola.desencolar()
			print(chr(e),end='')
			cola.encolar(e)

		indice += 1

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












