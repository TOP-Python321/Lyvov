fruit_list = []

while True:
    fruit = input(' Введите фрукт: ')
    if not fruit:
        break
    fruit_list.append(fruit)

if len(fruit_list) >= 2:
    fruit_list = fruit_list[:-2] + [' и '.join(fruit_list[-2:])]

print(*fruit_list, sep=', ')


#  Введите фрукт: яблоко
#  Введите фрукт: вишня
#  Введите фрукт: мандарин
#  Введите фрукт: виноград
#  Введите фрукт:
# яблоко, вишня, мандарин и виноград


