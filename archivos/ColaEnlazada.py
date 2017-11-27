from Nodo import Nodo

class ColaEnlazada:
	"""Representa a una cola, con operaciones de encolar y
	desencolar. El primero en ser encolado es también el primero
	en ser desencolado. """

	def __init__(self):
		"""Crea una cola vacía."""
		self.primero = None
		self.ultimo = None

	def __repr__(self):
		"""Muestra el contenido de la Cola Enlazada."""
		n_ant = self.primero
		nodos = ''
		delimitador = '->'
		while n_ant is not None:
			nodos += str(n_ant.dato)
			if n_ant.prox is not None:
				nodos += delimitador
			n_ant = n_ant.prox
		return nodos


	def encolar(self, x):
		"""Encola el elemento x."""
		nuevo = Nodo(x)
		if self.ultimo:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo
		else:
			self.primero = nuevo
			self.ultimo = nuevo

	def desencolar(self):
		"""Desencola el primer elemento y devuelve su
		valor. Si la cola está vacía, levanta ValueError."""
		if self.primero is None:
			raise ValueError("La cola está vacía")
		valor = self.primero.dato
		self.primero = self.primero.prox
		if not self.primero:
			self.ultimo = None
		return valor

	def esta_vacia(self):
		"""Devuelve True si la cola esta vacía, False si no."""
		return self.primero is None

	def ver_primero(self):
		"""Devuelve el primero de la Cola."""
		return self.primero.dato

	def incrementar_primero(self):
		"""Incrementa el primero, en caso de ser 256 incrementa 0."""
		dato = self.primero.dato
		self.primero.dato = (dato + 1) % 256 

	def decrementar_primero(self):
		"""Decrementa el primero, en caso de ser 0 decrementa 255"""
		dato = self.primero.dato
		self.primero.dato = (dato - 1) % 256 
