from ColaEnlazada import ColaEnlazada

class Interprete:
	"""..."""

	def __init__(self):
		"""..."""
		self.pos_act = 0
		self.cola = ColaEnlazada()
		self.contenido = ""
		self.dic = {}
		self.dic_aux = {}
		self.len = 0

		self.traduccion = ""

		#Encolar un 0 a la cola
		self.cola.encolar(0)


	def __str__(self):
		"""..."""
		return self.traduccion


	def __repr__(self):
		"""..."""
		return self.traduccion

	def leer_archivo(self,nombre_archivo):
		"""Recibe un archivo de tipo SCEQL y lo recorre caracter por caracter filtrando por los comandos validos del lenguaje SCEQL y lo almacena y self.contenido.
		Agregamos las posiciones de las barras en self.dic y self.dic_aux"""
		
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
					self.dic[self.len] = lista.pop()
				self.len += 1
		except ValueError:
			print("Archivo incorrecto")#No hay la misma cantidad de barras

		#Agregar al diccionario como clave la posicion de la barra que abre y el valor como la barra que cierra correspondiente
		for clave, valor in self.dic.items():
			self.dic_aux[valor] = clave

		#Chequear que lista esta vacia (no quedo ninguna barra sin pareja)
		if len(lista):
			raise ValueError("Archivo incorrecto.") #No hay la misma cantidad de barras

	def interpretar_valores(self):
		"""..."""

		indice = 0
		longitud = self.len
		cola_aux = ColaEnlazada()

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
					self.pos_act = self.dic_aux[self.pos_act] + 1
					continue

			elif char == '/':
				self.pos_act = self.dic[self.pos_act]
				continue

			elif char == '*':
				e = self.cola.desencolar()
				self.traduccion += chr(e)
				self.cola.encolar(e)

			self.pos_act += 1

	def interpretar_valores_debug(self):
		"""..."""

		indice = 0
		longitud = self.len
		cola_aux = ColaEnlazada()

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
					self.pos_act = self.dic_aux[self.pos_act] + 1
					continue

			elif char == '/':
				self.pos_act = self.dic[self.pos_act]
				continue

			elif char == '*':
				e = self.cola.desencolar()
				self.traduccion += chr(e)
				self.cola.encolar(e)

			ingreso = True
			while ingreso:
				input()
				print(self.cola)
				print(self.traduccion)
				print(self.contenido[:(self.pos_act + 1)% self.len])
				print(" "*self.pos_act + "^")

				ingreso = False

			self.pos_act += 1
