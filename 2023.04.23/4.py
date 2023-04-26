numbers = int (input ("Введите число: "))
 
for i in range (1, numbers // 2 + 1) :
  if numbers % i == 0 :
    print (i, i + numbers, sep = '', end = '')
print (numbers)

# Введите число: 7
# 187