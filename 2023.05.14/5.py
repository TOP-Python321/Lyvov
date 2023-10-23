def central_tendency(num1: float, num2: float, /, *numbers: float) -> dict[str, float]:
    """Вычисляет и возвращает словарь с подписанными вычисленными значениями мер центральной тенденции"""
    numbers = sorted((num1, num2) + numbers)
    length_numbers = len(numbers)
    middle_index = length_numbers // 2
    arithmetic = sum(numbers) / length_numbers
    product = 1
    numerator = 0
    
    if length_numbers % 2:
        median = float(numbers[middle_index])
    else:
        median = sum(numbers[middle_index-1 : middle_index+1]) / 2

    # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с произвольными числами
    for i in numbers:
        product *= i
        # ИСПРАВИТЬ: необходимо предусмотреть ноль среди чисел (см. тест ниже)
        numerator += 1 / i
        geometric = product ** (1 / length_numbers)
        harmonic = length_numbers / numerator

    # ИСПОЛЬЗОВАТЬ: не надо лишних переменных
    return {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }


# ИСПРАВИТЬ: выполняйте ручные тесты в режиме инспекции
print(central_tendency(1, 2, 3, 4))
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}

sample = [1, 2, 3, 4, 5]
print(central_tendency(*sample))
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

# >>> central_tendency(0, 1, -1, 2, -2)
# ...
# ZeroDivisionError: division by zero


# ИТОГ: хорошо, но можно лучше — 3/5
