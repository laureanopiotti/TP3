class Nodo:
	"""..."""
	def __init__(self, dato = None, prox = None, pos = 0):
		"""..."""
		self.dato = dato
		self.prox = prox
		self.pos = pos

	def __str__(self):
		"""..."""
		return str(self.dato)