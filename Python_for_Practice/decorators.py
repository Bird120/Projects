def voyage(pays):
	def mer():
		print("Going or Not going ?")
		pays()
		print("end")
	return mer

@voyage
def pays():
	print("Going on vacation: Greece")

@voyage
def rester():
	print("Not going on vacation")


pays()
print('\n')
rester()
