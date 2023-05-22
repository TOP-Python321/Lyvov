def central_tendency(num1: float, num2: float, / , *numbers: float) -> dict[str, float]:
    
    """Вычисляет и возвращает словарь с подписанными вычисленными значениями мер центральной тенденции"""

    numbers = sorted((num1, num2) + numbers)
    length_numbers = len(numbers)
    middle_index = length_numbers // 2
    arithmetic = sum(numbers) / length_numbers
    product = 1
    numerator= 0
    
    if length_numbers % 2:
        median = float(numbers[middle_index])
    else:
        median = sum(numbers[middle_index - 1 : middle_index + 1]) / 2
        
    for i in numbers:       
        product *= i 
        numerator += 1 / i
        geometric = product ** (1 / length_numbers)
        harmonic = length_numbers / numerator
    
    dict_tendency = {
                'median': median,
                'arithmetic': arithmetic,
                'geometric': geometric,
                'harmonic': harmonic
                }
                
    return dict_tendency
    
    
print(central_tendency(1, 2, 3, 4))
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}

sample = [1, 2, 3, 4, 5]
print(central_tendency(*sample))
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}