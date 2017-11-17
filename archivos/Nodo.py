class Nodo:
	"""Modela un Nodo"""
	def __init__(self, dato = None, prox = None, pos = 0):
		"""Constructor del Nodo"""
		self.dato = dato
		self.prox = prox
		self.pos = pos

	def __str__(self):
		"""Muestra el contenido del Nodo"""
		return str(self.dato)