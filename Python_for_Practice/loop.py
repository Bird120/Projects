import inspect

def manger(x):
	if x == "chocolat":
		def check():
			print("Elle/Il mange du chocolat.")
			def grossir():
				print("Je vais prendre 200 grammes.")
			grossir()
	else:
		def check():
			print("Elle/Il ne mange pas de chocolat.")
	return check

new_function = manger("chocolat")
new_function()
print(inspect.getmembers(new_function))