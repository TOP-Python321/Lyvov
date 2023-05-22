def strong_password(password: str) -> bool:
    
    """Возвращает объект bool: True - если пароль соответствует требованиям, False - не соответствует"""
    
    lower_letters = False
    upper_letters = False
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
        elif i.isdigit():
            digits = True
    
    if (len(password) >= 8 
        and upper_letters and lower_letters and spec and digits):
        return True
    else:
        return False
        
 
 
print(strong_password('aP3:kD_l3'))
# True

print(strong_password('password'))
# False