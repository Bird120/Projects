class Mylist:
	def __init__(self, mylist):
		self._list = mylist
		self._list_reverse = None

	@property
	def reverse(self):
		self._list_reverse = self._list[::-1]
		return self._list_reverse
	
	@reverse.setter
	def reverse(self, new_list):
		self._list = new_list

	
	def check_list(self):
		if not self._list:
			raise ValueError("Empty list")

