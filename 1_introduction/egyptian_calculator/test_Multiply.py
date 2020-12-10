from unittest import TestCase
from Multiply import Multiply


class TestMultiply(TestCase):
    def test_closest_number(self):
        calc = Multiply(33, 12)
        result = calc.closest_number(calc.num_b)
        self.assertEqual(result, 8)

    def test_calculate(self):
        calc = Multiply(12, 33)
        result = calc.calculate()
        self.assertEqual(result, 396)

    def test_cal(self):
        calc = Multiply(90, 127)
        result = calc.cal()
        self.assertEqual(result, [64, 32, 16, 8, 4, 2, 1])

