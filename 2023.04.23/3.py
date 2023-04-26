numbers = int(input("Введите натурально число: "))

summa = ([i for i in range(1, numbers + 1) if numbers % i == 0])

print(sum(summa))


# Введите натурально число: 60
# 168