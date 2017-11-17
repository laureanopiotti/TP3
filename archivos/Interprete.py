from ColaEnlazada import ColaEnlazada

class Interprete:
	"""Modela un Interprete SCEQL."""

	def __init__(self):
		"""Constructor del Interprete."""
		self.pos_act = 0
		self.cola = ColaEnlazada()
		self.contenido = ""
		self.barras_cerradas = {}
		self.barras_abiertas = {}
		self.len = 0

		self.traduccion = ""

		#Encolar un 0 a la ColaEnlazada
		self.cola.encolar(0)


	def __str__(self):
		"""Muestra la cadena traduccion"""
		return self.traduccion


	def __repr__(self):
		"""Muestra la cadena traduccion"""
		return self.traduccion

	def leer_archivo(self,nombre_archivo):
		"""Recibe un archivo de tipo SCEQL y lo recorre caracter por caracter filtrando por los comandos validos del lenguaje SCEQL y lo almacena en self.contenido.
		Agregamos las posiciones de las barras en self.barras_cerradas y self.barras_abiertas"""
		
		lista = []
		#Abrir el archivo a interpretar y obtener solo los caracteres permitidos por el lenguaje SCEQL
		try:
			with open(nombre_archivo) as archivo_a_recorrer:
				sceql_comandos = ['!','=','-','_','/','\\','*']
				for linea in archivo_a_recorrer:
					linea = linea.rstrip('/n').replace(' ','')
					for char in linea:
						if char in sceql_comandos:
							self.contenido += char
		except IOError:
			print("Problema con el archivo")
		
		try:
			#Agregar al diccionario como clave la posicion de la barra que cierra y el valor como la barra que abre correspondiente
			for char in self.contenido:
				if char == '\\':
					lista.append(self.len)
				elif char == '/':
					self.barras_cerradas[self.len] = lista.pop()
				self.len += 1
		except ValueError:
			print("Archivo incorrecto")#No hay la misma cantidad de barras

		#Agregar al diccionario como clave la posicion de la barra que abre y el valor como la barra que cierra correspondiente
		for clave, valor in self.barras_cerradas.items():
			self.barras_abiertas[valor] = clave

		#Chequear que lista esta vacia (no quedo ninguna barra sin pareja)
		if len(lista):
			raise ValueError("Archivo incorrecto.") #No hay la misma cantidad de barras

	def interpretar_valores(self, modo_debug):
		"""Recorre la cadena y dependiendo que es lo que encuntra va modificando la Cola Enlazada y el self.traduccion.
		Si el modo_debug es True entra en modo debug"""

		longitud = self.len

		while self.pos_act != (longitud - 1):
			char = self.contenido[self.pos_act]
			if char == '!':
				self.cola.encolar(0)

			elif char == '=':
				self.cola.encolar(self.cola.desencolar())

			elif char == '_':
				self.cola.incrementar_primero()

			elif char == '-':
				self.cola.decrementar_primero()

			elif char == '\\':
				e = self.cola.ver_primero()			
				if e == 0:
					self.pos_act = self.barras_abiertas[self.pos_act] + 1
					continue

			elif char == '/':
				self.pos_act = self.barras_cerradas[self.pos_act]
				continue

			elif char == '*':
				e = self.cola.desencolar()
				self.traduccion += chr(e)
				self.cola.encolar(e)

			if modo_debug:
				while True:
					print("Cola ",self.cola)
					print(self.traduccion)
					print(self.contenido[:(self.pos_act + 1)% self.len])
					print(" "*self.pos_act + "^")

					ingreso = input("Presione Enter para continuar")
					if ingreso == '':
						break

			self.pos_act += 1

		

