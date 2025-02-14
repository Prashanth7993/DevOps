import unittest

def add(a,b):
    return a+b


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3),5,"Add(2,3) returns some number other than 5")
    def test_add_positive_numbers(self):
        self.assertEqual(add(5,13),18,"Add(5,13) returns some number other than 18")



if __name__ == '__main__':
    unittest.main()