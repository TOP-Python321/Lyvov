from collections.abc import Iterable


def product(numbers: Iterable[float]) -> float:
    """
    Вычисляет произведение чисел.
    
    :param numbers: Итерируемый объект с числами в качестве элементов.
    
    :return: Float. Возвращает произведение чисел.
    """
    if len(numbers) == 0:
        return 1
    elif 0 in numbers:
        return 0.0
    return float(numbers[0]) * product(numbers[1:])
    
# print(product(range(10, 60, 10)))
# 12000000.0

# print(product((0.12, 0.05, -0.09, 0.0, 0.21)))
# 0.0