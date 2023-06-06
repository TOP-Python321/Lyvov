# УДАЛИТЬ: переменная inp избыточна
inp = input('Введите имена файлов: ')
list_inp = sorted(inp.split('; '))

list_cout = []
dict_copy = {}

for i in list_inp:
    dict_copy[i] = dict_copy.get(i, 0) + 1
    # КОММЕНТАРИЙ: хорошо, что в один цикл пошли
    if dict_copy[i] == 1:
        list_cout.append(i)
    else:
        # ИСПРАВИТЬ: метод index() вызывается лишний раз — оптимизируйте
        list_cout.append(i[:i.index('.')] + '_' + str(dict_copy[i]) + i[i.index('.'):])

print(*list_cout, sep='\n')


# Введите имена файлов: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz


# ИТОГ: хорошо, требуется немного доработать — 4/6
