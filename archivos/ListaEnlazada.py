from Nodo import _Nodo
from IteradorListaEnlazada import _IteradorListaEnlazada

class ListaEnlazada:
	"""Modela una lista enlazada."""
	def __init__(self):
		"""Crea una lista enlazada vacía."""
		# referencia al primer nodo (None si la lista está vacía)
		self.prim = None
		# cantidad de elementos de la lista
		self.longitud = 0

	def __str__(self):
		"""Muestra la lista"""
		"""Recorre todos los nodos a través de sus enlaces, mostrando sus contenidos."""
		n_ant = self.prim
		nodos = ''
		delimitador = '-->'
		while n_ant is not None:
			nodos += str(n_ant.dato)
			if n_ant.prox is not None:
				nodos += delimitador
			n_ant = n_ant.prox
		return nodos

	def __iter__(self):
		"""Devuelve un iterador de la lista."""
		return _IteradorListaEnlazada(self.prim)

	def len(self):
		return self.longitud

	"""def longLista(self):
		return self.len"""

	def pop(self, i = None):
		"""Elimina el nodo de la posición i, y devuelve el dato contenido. Si i está fuera de rango, se levanta la excepción IndexError. Si no se recibe la posición, devuelve el último elemento."""
		if i is None:
			i = self.longitud - 1
		if i < 0 or i >= self.longitud:
			raise IndexError("Índice fuera de rango")
		if i == 0:
			# Caso particular: saltear la cabecera de la lista
			dato = self.prim.dato
			self.prim = self.prim.prox
		else:
			# Buscar los nodos en las posiciones (i-1) e (i)
			n_ant = self.prim
			n_act = n_ant.prox
			for pos in range(1, i):
				n_ant = n_act
				n_act = n_ant.prox
			# Guardar el dato y descartar el nodo
			dato = n_act.dato
			n_ant.prox = n_act.prox
		self.longitud -= 1
		return dato

	def remove(self, x):
		"""Borra la primera aparición del valor x en la lista. Si x no está en la lista, levanta ValueError"""
		if self.longitud == 0:
			raise ValueError("Lista vacía")
		if self.prim.dato == x:
			#Caso particular: saltear la cabecera de la lista
			self.prim = self.prim.prox
		else:
			#Buscar el nodo anterior al que contiene a x (n_ant)
			n_ant = self.prim
			n_act = n_ant.prox
			while n_act is not None and n_act.dato != x:
				n_ant = n_act
				n_act = n_ant.prox
			if n_act == None:
				raise ValueError("El valor no está en la lista.")
			# Descartar el nodo
			n_ant.prox = n_act.prox
		
		self.longitud -= 1

	def insert(self, i, x):
		"""Inserta el elemento x en la posición i. Si la posición es inválida, levanta IndexError"""
		if i < 0 or i > self.longitud:
			raise IndexError("Posición inválida")
		nuevo = _Nodo(x)
		if i == 0:
			# Caso particular: insertar al principio
			nuevo.prox = self.prim
			self.prim = nuevo
		else:
			# Buscar el nodo anterior a la posición deseada
			n_ant = self.prim
			for pos in range(1, i):
				n_ant = n_ant.prox
			# Intercalar el nuevo nodo
			nuevo.prox = n_ant.prox
			n_ant.prox = nuevo
		self.longitud += 1

	def append(self, x):
		"""Inserta un elemento x en la ultima posicion"""

		#defino el nuevo nodo
		nuevo = _Nodo(x)

		#Si la lista enlazada está vacia

		if self.longitud == 0:
			self.prim = nuevo
		else:
			n_act = self.prim
			while n_act.prox:
				n_act = n_act.prox

			n_act.prox = nuevo

		self.longitud += 1

	#Metodo (Estructura interna de la class)
	def extender(self, lista_a_agregar):
		if not lista_a_agregar.prim:
			return 

		actual_nueva = lista_a_agregar.prim #Me paro en el primer nodo de B
		
		primero_nuevo = _Nodo(actual_nueva.dato) #Creo el dato de B colgado en el aire
		
		actual = primero_nuevo #Miro al primer nodo de A
		
		actual_nueva = actual_nueva.prox #Paso a mi nodo de B siguiente
		
		while actual_nueva: #Entro en ciclo mientras YO este parado en un nodo, para agregarlos a mi nodo creado
			
			nodo = _Nodo(actual_nueva.dato)

			actual.prox = nodo #Digo que el SIGUIENTE A LA LISTA A es mi nodo

			actual = actual.prox #Me paro en mi siguiente nodo(El nuevo que cree)

			actual_nueva = actual_nueva.prox #Paso al siguiente de B

		if self.prim is None:
			
			self.prim = primero_nuevo
		else:
			actualA = self.prim
			
			while actualA.prox: #Me paro en el ultimo nodo, hasta que el siguiente
				actualA = actualA.prox

			actualA.prox = primero_nuevo
			
		self.longitud += lista_a_agregar.longitud

	def invertir(self):
		#Defino mis variables
		anterior = None
		actual = self.prim
		siguiente = actual.prox

		while actual:#Donde estoy parado

			#Voy moviendome para ir cambiando las referencias
			actual.prox = anterior #El siguiente a mi actual es mi anterior
			anterior = actual  
			actual = siguiente

			if siguiente:#Tengo siguiente? Si, entonces lo apunto a su siguiente
				siguiente=siguiente.prox

		self.prim = anterior