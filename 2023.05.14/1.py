def strong_password(password: str) -> bool:
    """Возвращает объект bool: True - если пароль соответствует требованиям, False - не соответствует"""
    lower_letters = False
    upper_letters = False
    # ИСПРАВИТЬ: мало символов
    symbols = "-+*=~!:@#$%^&()/|"
    spec = False
    digits = False
    
    for i in password:
        if i.islower():
            lower_letters = True
        elif i.isupper():
            upper_letters = True
        elif i in symbols:
            spec = True
        # ИСПРАВИТЬ: в пароле должно быть от двух цифр (см. тест ниже)
        elif i.isdigit():
            digits = True

    # УДАЛИТЬ: условная конструкция избыточна
    # ИСПОЛЬЗОВАТЬ: скобки избыточны
    if len(password) >= 8 and upper_letters and lower_letters and spec and digits:
        return True
    else:
        return False


# ИСПРАВИТЬ: выполняйте ручные тесты в режиме инспекции
print(strong_password('aP3:kD_l3'))
# True

print(strong_password('password'))
# False

# >>> strong_password('aaaaBBBB4!')
# КОММЕНТАРИЙ: должно быть False
# True

# КОММЕНТАРИЙ: рассмотрено мало вариантов пароля


# ИТОГ: нужно лучше, доработать — 2/4
