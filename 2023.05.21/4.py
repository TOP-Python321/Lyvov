def repeat(func: 'callable') -> 'callable':
    """
    Выполняет декорируемую функцию десять раз.
    :param func: декорируемая функция
    :return: функция-обёртка
    """
    def wrapper(*args, **kwargs):
        for _ in range(10):
            # УДАЛИТЬ: print() не нужен
            print(func(*args, **kwargs))
    return wrapper


def testing_function():
    return 'I will learn and I will learn'

# testing_function = repeat(testing_function)
# testing_function()

# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn
# I will learn and I will learn


# ИТОГ: хорошо — 3/3
