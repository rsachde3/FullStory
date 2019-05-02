import unittest
from Multiply import multiply, multiplyShift


class TestMultiplication(unittest.TestCase):

#Test cases for the function Multiply
    def test_multiply(self):
        res = multiply(3, 5)
        self.assertEqual(res, 15)
        res = multiply(-7, -4)
        self.assertEqual(res, 28)
        res = multiply(-6, 4)
        self.assertEqual(res, -24)
        res = multiply(5, -4)
        self.assertEqual(res, -20)
        res = multiply(0, 5)
        self.assertEqual(res, 0)

#Test cases for the function MultiplyShift
    def test_shift_multiply(self):
        res = multiplyShift(3, 5)
        self.assertEqual(res, 15)
        res = multiplyShift(-7, -4)
        self.assertEqual(res, 28)
        res = multiplyShift(-6, 4)
        self.assertEqual(res, -24)
        res = multiplyShift(5, -4)
        self.assertEqual(res, -20)
        res = multiplyShift(0, 5)
        self.assertEqual(res, 0)

#Test cases to check for value errors
    def test_error(self):
        self.assertRaises(ValueError, multiply, "re", "re")
        self.assertRaises(ValueError, multiply, 5, 5.09)
        self.assertRaises(ValueError, multiplyShift, "re", "re")
        self.assertRaises(ValueError, multiplyShift, 5, 5.09)

if __name__ == '__main__':
    unittest.main()