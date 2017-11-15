class _IteradorListaEnlazada:
	"""..."""
	def __init__(self, prim):
		"""..."""
		self.actual = prim

	def __next__(self):
		"""..."""
		if self.actual is None:
			raise StopIteration()

		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato
