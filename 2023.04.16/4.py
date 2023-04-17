first_cell = input("Укажите первую клетку: ")
second_cell = input("Укажите вторую клетку: ")

color_1 = (ord(first_cell[0]) + int(first_cell[1])) % 2
color_2 = (ord(second_cell[0]) + int(second_cell[1])) % 2

if color_1 == color_2:
    print("Да")
else:
    print("Нет")
    
# Укажите первую клетку: c7
# Укажите вторую клетку: g1
# Да