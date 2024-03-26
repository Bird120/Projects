class Order:
	def __init__(self, value):
		self._value = value

	def __pow__(self, other=None):
		print('self._value: ', self._value)
		if other is None:
			other = self._value
		return self._value ** other


x = Order(4)

print(x)

z = x ** None

result = x ** 3

print(z)
print(result)