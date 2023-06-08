import unittest
import math

from functions import is_prime, square, bank
from exceptions import (SideNegativeValueException,
                        YearsNegativeValueException,
                        DepositNegativeValueException)


class TestIsPrimeFunction(unittest.TestCase):
    """Тестирование функции is_prime."""

    def test_list_of_numbers_for_prime(self):
        """Проверить, что числа из списка являются простыми."""
        values_list = (-8, -3, 0, 1, 2, 3, 4, 7, 10, 13, 100)
        expected_results_list = (False, False, False, False, True, True, False,
                                 True, False, True, False)
        for number, expected_result in zip(values_list, expected_results_list):
            with self.subTest(f'Ошибка для числа {number}'):
                self.assertEqual(is_prime(number), expected_result)


class TestSquareFunction(unittest.TestCase):
    """Тестирование функции square."""

    def test_positive_side(self):
        """Рассчитать периметр, площадь и диагональ квадрата для положительного
        значения стороны."""
        side_values = (1, 2, 5)
        expected_results = ((4, 1, math.sqrt(2)),
                            (8, 4, math.sqrt(2)*2),
                            (20, 25, math.sqrt(2) * 5))
        for side, expected_results in zip(side_values, expected_results):
            with self.subTest(f'Ошибка для стороны: {side}'):
                self.assertEqual(square(side), expected_results)

    def test_zero_side(self):
        """Рассчитать периметр, площадь и диагональ квадрата для стороны 0"""
        result = square(0)
        expected_result = (0, 0, 0)
        self.assertEqual(result, expected_result)

    def test_negative_side(self):
        """Рассчитать периметр, площадь и диагональ квадрата для отрицательного
        значения стороны."""
        side = -3
        with self.assertRaises(SideNegativeValueException):
            square(side)


class TestBankFunction(unittest.TestCase):
    """Тестирование функции bank."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.summa = 100

    def test_positive_years_amount(self):
        """Рассчитать итоговую сумму на вкладе за положительное
        количество лет."""
        years_list = (1, 3, 10)
        expected_result = (110, 133.1, 259.374246)
        for year, expected_result in zip(years_list, expected_result):
            with self.subTest(f'Ошибка при количестве лет: {year}'):
                self.assertEqual(round(bank(self.summa, year), 2),
                                 round(expected_result, 2)
                                 )

    def test_zero_years(self):
        """Рассчитать итоговую сумму на вкладе за 0 лет"""
        years_amount = 0
        result = bank(self.summa, years_amount)
        self.assertEqual(result, self.summa)

    def test_negative_years_amount(self):
        """Рассчитать итоговую сумму на вкладе за отрицательное
        количество лет."""
        years_amount = -2
        with self.assertRaises(YearsNegativeValueException):
            bank(self.summa, years_amount)

    def test_negative_summa(self):
        """Рассчитать итоговую сумму на вкладе за отрицательное
        количество лет."""
        summa = -2
        years_amount = 10
        with self.assertRaises(DepositNegativeValueException):
            bank(summa, years_amount)


if __name__ == "__main__":
    unittest.main()
