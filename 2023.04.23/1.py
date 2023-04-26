num = []
while True:
    numbers = input("Введите целое число кратное 7: ")
    if int(numbers) % 7 == 0:
        num.append(numbers)
        continue
    else:
        digits = list(reversed(num))
        print(" ".join(digits))
        break
        
# Введите целое число кратное 7: 7
# Введите целое число кратное 7: 21
# Введите целое число кратное 7: 28
# Введите целое число кратное 7: 35
# Введите целое число кратное 7: 7
# Введите целое число кратное 7: 33
# 7 35 28 21 7