minutes_inp = int(input("Введите количество минут: "))

# КОММЕНТАРИЙ: избыточные переменные
hour = minutes_inp // 60
minutes = minutes_inp % 60

print(f"{minutes_inp} мин - это {hour} час {minutes} мин")

# Введите количество минут: 105
# 105 мин - это 1 час 45 мин


# ИТОГ: отлично — 3/3
