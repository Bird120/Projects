from mylist import Mylist
import unittest


class Testlist(unittest.TestCase):
	def test_list(self):
		original = "Vile1234"
		print("test original list: " , original)
		list1 = Mylist(original)
		self.assertTrue(list1)
		print("\ntest: ",list1.reverse)


	def test_null(self):
		original = ""
		print("\n\ntest original list:", original)
		empty_list = Mylist(original)
		with self.assertRaises(ValueError):
			empty_list.check_list()


if __name__ == '__main__':
    unittest.main()