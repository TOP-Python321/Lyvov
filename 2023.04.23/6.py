ticket = [int(char) for char in input("Введите номер билета: ")]
if sum(ticket[:3]) == sum(ticket[3:]):
    print('Да')
else:
    print('Нет')


# Введите номер билета: 645708
# Да

# Введите номер билета: 956234
# Нет


# ИТОГ: отлично — 3/3
