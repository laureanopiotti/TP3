class _IteradorListaEnlazada:
	"""..."""
	def __init__(self, prim):
		"""..."""
		self.actual = prim
		self.indice = 0

	def __next__(self):
		"""..."""
		if self.actual is None:
			raise StopIteration()

		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato

	def prev(self):
		"""..."""

