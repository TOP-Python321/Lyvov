# ИСПОЛЬЗОВАТЬ здесь и далее везде: откуда лишние пробелы в коде повылазили? оформляем по PEP 8
number = int(input("Введите число: "))

# КОММЕНТАРИЙ: вот такой диапазон для поиска делителей уже намного лучше, примените в предыдущей задаче
# КОММЕНТАРИЙ: а для поиска простых чисел, вам не нужно проверять делимость на единицу, потому что на неё делятся без остатка все целые числа
for i in range(1, number//2 + 1):
    if number % i == 0:
        # ОТВЕТИТЬ: это что вы выводите?
        print(i, i+number, sep='', end='')
print(number)

# КОММЕНТАРИЙ: вспомните, что такое разряд числа: числа одной разрядности — это от 1 до 9, от 10 до 99, от 100 до 999 и так далее
# КОММЕНТАРИЙ: на будущее: если не понимаете, что от вас требуется в задаче, то уточните у меня в личном чате Teams


# Введите число: 7
# 187


# ИТОГ: задача не понята, переделать — 0/4
