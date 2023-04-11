num_input = int(input("Введите трехзначное число: "))

num = num_input // 10
num_one = num // 10
num_two = num % 10
num_three = num_input % 10

# Сумма цифр
sum_num = num_one + num_two + num_three

# Произведение цифр
multi_num = num_one * num_two * num_three


print(f"Сумма цифр = {sum_num} \nПроизведение цифр = {multi_num}")

# Введите трехзначное число: 555
# Сумма цифр = 15
# Произведение цифр = 125