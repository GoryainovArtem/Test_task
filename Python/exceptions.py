class SideNegativeValueException(ValueError):
    """
    Исключение при использовании отрицательного значения
    для стороны квадрата.
    """

    def __str__(self):
        return ('Значение стороны квадрата должно '
                'быть положительным числом.'
                )


class DepositNegativeValueException(ValueError):
    """
    Исключение при использовании отрицательного значения
    для суммы вклада.
    """

    def __str__(self):
        return ('Сумма для вклада должна быть '
                'положительным числом.'
                )


class YearsNegativeValueException(ValueError):
    """
    Исключение при использовании отрицательного значения
    для количества лет.
    """

    def __str__(self):
        return ('Количество лет должно быть '
                'положительным числом.'
                )
