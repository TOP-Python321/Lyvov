num = int(input("Введите целое число: "))

# КОММЕНТАРИЙ: объявление данных переменных можно считать избыточным, если принять во внимание простоту используемых выражений и то, что в дальнейшем каждая из переменных используется только единожды
back_num = num - 1
next_num = num + 1

# ИСПОЛЬЗОВАТЬ: альтернативный вариант записи строковых литералов в несколько строчек (только внутри скобок)
print(f" Следующее за числом {num} число: {next_num} \n"
      f" Для числа {num} предыдущее число: {back_num}")

# Введите целое число: 50
#  Следующее за числом 50 число 51
#  Для числа 50 предыдущее число: 49


# ИТОГ: отлично — 3/3
