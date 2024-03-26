class Order:
    def __init__(self, number):
        self._value = number

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, number):
        print("Setting value...")
        self._value = number

    @value.getter
    def value(self):
    	print("Getting value...")
    	return self._value


    def __pow__(self, other=None):
        if other is None:
            other = self._value
        return self._value ** other

x = Order(2)
print(x.value)
x.value = 5
print(x.value)
z = x ** None
b = x ** 3
print(z, b)

