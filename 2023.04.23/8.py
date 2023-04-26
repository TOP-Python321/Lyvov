element = int(input("Введите элемент последовательности: "))

number_1 = number_2 = 1
print(number_1, number_2, end = ' ')

i = 2

while i < element:
    number_1, number_2 = number_2, number_1 + number_2
    print(number_2, end = ' ')
    i += 1
    
# Введите элемент последовательности: 23
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657