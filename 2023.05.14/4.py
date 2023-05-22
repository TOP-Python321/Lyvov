def countable_nouns(number: int, words: tuple[str, str, str]) -> str:

    """Возвращает строку, которая согласуется с переданным аргументом number"""
         
    list1= [2, 3, 4]
    list2 = [0, 5, 6, 7, 8, 9]

    if 11 <= number % 100 <=14:
        return words[2]
    elif number % 10 in list1:
        return words[1]
    elif number % 10 in list2:
        return words[2]
    else:
        return words[0]
        
        
print(countable_nouns(1, ("год", "года", "лет")))
# 'год'
print(countable_nouns(2, ("год", "года", "лет")))
# 'года'
print(countable_nouns(10, ("год", "года", "лет")))
# 'лет'
print(countable_nouns(12, ("год", "года", "лет")))
# 'лет'
print(countable_nouns(22, ("год", "года", "лет")))
# 'года'