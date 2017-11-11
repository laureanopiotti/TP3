class Pila:
	"""Representa una pila con operaciones de apilar, desapilar, verificar si está vacía y ver tope."""
	def __init__(self):
		"""Crea una pila vacía."""
		self.items = []

	def esta_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.items) == 0

	def apilar(self, x):
		"""Apila el elemento x."""
		self.items.append(x)

	def desapilar(self):
		"""Devuelve el elemento tope y lo elimina de la pila. Si la pila está vacía levanta una excepción."""
		if self.esta_vacia():
			raise IndexError("La pila está vacía")
		return self.items.pop()

	def ver_tope(self):
		"""Devuelve el tope de la pila."""
		if not self.esta_vacia:
			return "La pila esta vacia."
		return self.items[-1]