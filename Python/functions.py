from exceptions import (YearsNegativeValueException,
                        DepositNegativeValueException,
                        SideNegativeValueException)


def is_prime(number: int) -> bool:
    """
    Проверить, что передаваемый аргумент является
    натуральным числом.
    :param number:
    :return:
    """
    import math

    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def square(side: int | float) -> tuple[int | float,
                                       int | float,
                                       int | float]:
    """
    Рассчитать периметр, площадь, диагональ по
    известной стороне.
    :param side:
    :return:
    """
    if side < 0:
        raise SideNegativeValueException
    import math

    return 4 * side, side ** 2, side * math.sqrt(2)


def bank(a: int | float, years: int) -> int | float:
    """
    Рассчитать сумму, которая будет на счету пользователя
    через years лет при 10% годовых и вкладе a рублей.
    :param a:
    :param years:
    :return:
    """
    from functools import reduce

    if years < 0:
        raise YearsNegativeValueException
    if a < 0:
        raise DepositNegativeValueException
    return reduce(lambda x, y: x * 1.1, range(years), a)
