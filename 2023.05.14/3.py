# ДОБАВИТЬ: полную аннотацию возвращаемого значения
def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list:
    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или изменённую копию"""
    # КОММЕНТАРИЙ: вы вносите изменения в переданный список, даже если функция была вызвана с copy=True (см. тест ниже)
    while n > 0:
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))
        n -= 1 

    # ИСПРАВИТЬ: эта часть должна быть в начале тела функции
    if copy:
        return numbers.copy()
    else:
        return numbers


# ИСПРАВИТЬ: выполняйте ручные тесты в режиме инспекции
# sample = [1, 2, 3, 4]
# sample_stripped = numbers_strip(sample)
# print(sample_stripped)
# print(sample is sample_stripped)
# [2, 3]
# True

# sample = [10, 20, 30, 40, 50]
# sample_stripped = numbers_strip(sample, 2, copy=True)
# print(sample_stripped)
# print(sample is sample_stripped)
# [30]
# False

# >>> sample = [-1, 0, 1]
# >>> numbers_strip(sample, 1, copy=True)
# [0]
# >>> sample
# [0]


# ИТОГ: нужно лучше, доработать — 2/4
