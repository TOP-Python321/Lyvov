whole_mil = int(input("Введите целую часть мили: "))
fractional_mil = int(input("Введите дробную часть мили: "))

one_mil = 1.61

# ИСПРАВИТЬ: скобки вокруг f-строки не нужны
mil = float((f"{whole_mil}.{fractional_mil}"))
km = round(one_mil * mil, 1)

print(f"{mil} миль = {km} км")

# Введите целую часть мили: 18
# Введите дробную часть мили: 2
# 18.2 миль = 29.3 км


# ИТОГ: отлично — 4/4
