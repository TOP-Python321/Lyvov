numbers = int(input("Введите натурально число: "))

numbers_sum =0

while True:
    numbers_int = input("Введите целое число: ")
    if numbers_int == "quit":
        print(numbers_sum)
        break
    elif int(numbers_int) > 0:
        numbers_sum += int(numbers_int)
        continue
        
        
# Введите натурально число: 8
# Введите целое число: 3
# Введите целое число: -4
# Введите целое число: 7
# Введите целое число: -2
# Введите целое число: -6
# Введите целое число: 11
# Введите целое число: 4
# Введите целое число: quit
# 25