case = {}

while True:
    inp = input('Введите число через пробел: ')
    if not inp:
        break
    # УДАЛИТЬ: избыточная переменная — к пустой строке тоже можно применить метод split() — он вернёт пустой список
    list_inp = inp.split()
    case[list_inp[0]] = list_inp[1]

inp_value = input('Введите значение из словаря: ')
for k, v in case.items():
    if v == inp_value:
        print(k)
        break
# КОММЕНТАРИЙ: вот это хорошо!
else:
    print('! value error !')


# Введите число через пробел: 789 Брус
# Введите число через пробел: 689 Рейка
# Введите число через пробел: 569 Шифер
# Введите число через пробел: 878 Кирпич
# Введите число через пробел:
# Введите значение из словаря: Рейка
# 689

# Введите число через пробел: 789 Брус
# Введите число через пробел: 689 Рейка
# Введите число через пробел: 569 Шифер
# Введите число через пробел: 878 Кирпич
# Введите число через пробел:
# Введите значение из словаря: Гвоздь
# ! value error !


# ИТОГ: очень хорошо — 3/4
