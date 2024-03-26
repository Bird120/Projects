class calculator:
	def __init__(self, number1, number2):
		self.number1 = number1
		self.number2 = number2

	def __mul__(self):
		return self.number1 * self.number2

	def __add__(self):
		return self.number1 + self.number2

	def __sub__(self):
		return self.number2 - number1


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
p = calculator(number1,number2)
print("Add: ", p.__add__(), "Sub: ",p.__sub__(), "Mul: ", p.__mul__())
