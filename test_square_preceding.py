import unittest
from square_preceding import square_preceding

class TestSquareMethods(unittest.TestCase):
    def test_basic_numbers(self):
        test_list = [2 ,4 ,5]
        self.assertEqual(square_preceding(test_list), [0,4,16])

    def test_empty_list(self):
        test_list2=[]
        self.assertEqual(square_preceding(test_list2), [])

    def test_negative_numbers(self):
        test_list3=[-2, -3, -4]
        self.assertEqual(square_preceding(test_list3), [0,4,16])


if __name__ == "__main__":
    unittest.main()