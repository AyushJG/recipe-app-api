"""
Sample Test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)

    def test_multiply_numbers(self):
        res = calc.multiply(5, 5)
        self.assertEqual(res, 25)

    def test_divide_numbers(self):
        res = calc.divide(10, 2)
        self.assertEqual(res, 5)
