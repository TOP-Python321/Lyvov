emai_user = input("Введите свой email: ")

if emai_user[0] != '@' and emai_user.count('.') > 0 and emai_user.rfind('.') > emai_user.find('@'):
    print("Да")
else:
    print("Нет")
    
# Введите свой email: maratal@ya.ru
# Да
# Введите свой email: maratal.ya@ff
# Нет
# Введите свой email: maratal@lop
# Нет