def math_function_resolver(
        math_function: 'callable',
        *args: tuple[float],
        strings: bool = False
) -> list[float | str]:
    """
    Вычисляет округлённые значения для различных математических функций.
    
    :param math_function: Вызываемый объект. Ожидает один обязательный аргумент.
    :param args: Кортеж с аргументами. Каждый аргумент будет передан в функцию для вычисления.
    :param strings: Опциональный параметр. Возвращает строковое представление результатов вычисления, если True, иначе возвращает float.
    :return: Список результатов вычисления переданной функции.
    """
    result = []
    for num in args:
        result.append(round(math_function(num), 2))
    # КОММЕНТАРИЙ: вместо ещё одной итерации по списку результатов, можно использовать более эффективный подход (см. референс)
    return [str(num) for num in result] if strings else result


# print(math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10)))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]

# print(math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10)))
# [1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]


# ИТОГ: хорошо — 3/3
