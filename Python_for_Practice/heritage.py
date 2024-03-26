
class Foo:
	def show(self):
		print("Hi")

def add_attribute(self):
	self.z = 9


Test = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})
t = Test()
t.add_attribute()
t.wy = "Hello"
print(t.z)