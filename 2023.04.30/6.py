inp = input('Введите строку: ')

set_inp = set(inp)
binary_set_nums = {'0', '1', 'b'}

if (not (set_inp <= binary_set_nums)
   or inp.count('b') > 1 
   or 'b' in inp and '1' in inp[:inp.index('b')]
   # эти проверки возможно лишние
   or 'b' in inp and len(inp) == 1
   or '0b' in inp and len(inp) == 2
   ):
    print('Нет')
    
else:
    print('Да')
    
# Введите строку: 1b0101
# Нет