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
        raise ValueError('Значение стороны квадрата должно быть '
                         'положительным числом.')
    import math
    return 4 * side, side ** 2, side * math.sqrt(2)


def bank(a: int | float, years: int) -> int | float:
    """Рассчитать сумму, которая будет на счету пользователя
    через years лет при 10% годовых и вкладе a рублей."""
    if years < 0:
        raise ValueError('Количество лет должно быть '
                         'положительным числом')
    if a < 0:
        raise ValueError('Сумма для инвестиции должна быть '
                         'положительным числом')
    for i in range(years):
        a *= 1.1
    return a
