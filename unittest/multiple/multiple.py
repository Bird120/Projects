class Multiple:
	def __init__(self, number1, number2):
		self._number1 = number1
		self._number2 = number2

	@property
	def values(self):
		return (self._number1, self._number2)

	@values.setter
	def values(self, values_tuple):
		self._number1, self._number2 = values_tuple

	def calcul(self):
		return self._number1 * self._number2
