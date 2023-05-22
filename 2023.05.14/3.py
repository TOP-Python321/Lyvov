def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list:

    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или изменённую копию"""
     
    while n > 0:
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))
        n -= 1 
        
    if copy:
        return numbers.copy()
    else:
        return numbers
        
        
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