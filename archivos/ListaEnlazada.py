from Nodo import _Nodo
from IteradorListaEnlazada import _IteradorListaEnlazada

class ListaEnlazada:
	"""Modela una lista enlazada."""
	def __init__(self):
		"""Crea una lista enlazada vacía."""
		# referencia al primer nodo (None si la lista está vacía)
		self.prim = None
		# referencia al indice de la lista enlazada
		self.index = 0
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

	def __repr__(self):
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

			nuevo.pos = self.longitud
			n_act.prox = nuevo

		self.longitud += 1

	def jose(self,indice):
		"""..."""

		if self.longitud == 0:
			raise ValueError('La ListaEnlazada esta vacia')

		else:
			n_act = self.prim
			while n_act.pos != indice:
				n_act = n_act.prox

		return n_act.dato




