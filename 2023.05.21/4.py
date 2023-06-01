def repeat(func: 'callable') -> 'callable':
    """
    Выполняет декорируемую функцию десять раз.
    :param func: Вызываемый объект.
    :return: Возвращает Декорируемую функцию.
    
    """
    def wrapper(*args, **kwargs):
        for i in range(10):
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