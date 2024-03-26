import unittest
from multiple import Multiple

class TestMultiple(unittest.TestCase):
	def test_(self):
		multiple1 = Multiple(6,5)
		multiple2 = Multiple(5,6)
		self.assertEqual(multiple1.calcul(), multiple2.calcul())
		print("test: ",multiple1.values)

		multiple1.values = (2, 4)
		print("test2: ",multiple1.values)
		self.assertNotEqual(multiple1.calcul(), multiple2.calcul())


if __name__=='__main__':
	unittest.main()