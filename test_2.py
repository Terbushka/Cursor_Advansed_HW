import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 2), 4)
        self.assertEqual(Calculator.add(-2, 5), 3)
        self.assertEqual(Calculator.add(0, 5), 5)
        self.assertEqual(Calculator.add(5.5, 5), 10.5)
        self.assertRaises(TypeError, Calculator.add, "a", 5)
        self.assertRaises(TypeError, Calculator.add, None, 5)
        self.assertRaises(TypeError, Calculator.add, {}, 5)
        self.assertRaises(TypeError, Calculator.add, [1, 2], 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(2, 2), 0)
        self.assertEqual(Calculator.subtract(-2, 5), -7)
        self.assertEqual(Calculator.subtract(0, 5), -5)
        self.assertEqual(Calculator.subtract(10.5, 5), 5.5)
        self.assertRaises(TypeError, Calculator.subtract, "a", 5)
        self.assertRaises(TypeError, Calculator.subtract, None, 5)
        self.assertRaises(TypeError, Calculator.subtract, {}, 5)
        self.assertRaises(TypeError, Calculator.subtract, [1, 2], 5)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)
        self.assertEqual(Calculator.multiply(-2, 5), -10)
        self.assertEqual(Calculator.multiply(0, 5), 0)
        self.assertEqual(Calculator.multiply(5.5, 5), 27.5)
        self.assertEqual(Calculator.multiply("a", 5), "aaaaa")
        self.assertEqual(Calculator.multiply([1, 2], 5), [1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
        self.assertRaises(TypeError, Calculator.multiply, None, 5)
        self.assertRaises(TypeError, Calculator.multiply, {}, 5)

    def test_divide(self):
        self.assertEqual(Calculator.divide(2, 2), 1)
        self.assertEqual(Calculator.divide(-10, 5), -2)
        self.assertEqual(Calculator.divide(0, 5), 0)
        self.assertEqual(Calculator.divide(10, 0.5), 20)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)
        self.assertRaises(TypeError, Calculator.divide, "a", 5)
        self.assertRaises(TypeError, Calculator.divide, [1, 2], 5)
        self.assertRaises(TypeError, Calculator.divide, None, 5)
        self.assertRaises(TypeError, Calculator.divide, {}, 5)