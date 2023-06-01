inp_1 = input("Введите числа через пробел: ").split()
inp_2 = input("Введите числа через пробел: ").split()

print_out = 'Нет'
list_1, list_2 = [int(i) for i in inp_1], [int(i) for i in inp_2]

if not list_2:
    print_out = 'Да'
else:
    for i in range(len(list_1)):
        for k in list_1:
            if list_1[i] == k and list_2 == list_1[i:i+len(list_2)]:
                print_out = 'Да'
                break

print(print_out)


# Введите числа через пробел: 5 6 7 8
# Введите числа через пробел: 7 8
# Да
# Введите числа через пробел: 5 6 7 8
# Введите числа через пробел: 5 8
# Нет


