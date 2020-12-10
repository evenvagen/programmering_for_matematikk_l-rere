from unittest import TestCase
from Multiply import Multiply


class TestMultiply(TestCase):
    def test_closest_number(self):
        calc = Multiply(33, 12)
        result = calc.closest_number(calc.num_b)
        self.assertEqual(result, 8)

    def test_calculate(self):
        calc = Multiply(12, 33)
        result = calc.beta_calculator()
        self.assertEqual(result, 396)

    def test_cal_simple(self):
        calc = Multiply(8, 7)
        numbers = calc.egypt_calculator()
        self.assertEqual(numbers, [32, 16, 8])

    def test_cal(self):
        calc = Multiply(90, 127)
        numbers = calc.egypt_calculator()
        sum_of_nums = sum(numbers)
        self.assertEqual(numbers, [5760, 2880, 1440, 720, 360, 180, 90])
        self.assertEqual(sum_of_nums, 11430)

