class Cola:
	"""Representa a una cola, con operaciones de encolar, desencolar, ver si esta vacia o no y ver primero. El primero en ser encolado es también el primero en ser desencolado."""
	def __init__(self):
		"""Crea una cola vacía."""
		self.items = []
		self.pos_actual = 0

	def __str__(self):
		"""Muestra la cola"""
		return str(self.items)

	def encolar(self, x):
		"""Encola el elemento x."""
		self.items.append(x)
		self.pos_actual += 1

	def desencolar(self):
		"""Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError."""
		if self.esta_vacia():
			raise ValueError("La cola está vacía")
		return self.items.pop(0)
		self.pos_actual -= 1

	def esta_vacia(self):
		"""Devuelve True si la cola esta vacía, False si no."""
		return len(self.items) == 0

	def ver_primero(self):
		"""Devuelve el tope de la Cola."""
		if not self.esta_vacia:
			return "La pila esta vacia."
		return self.items[0]

	def ver_pos_actual(self):
		"""..."""
		return self.pos_actual