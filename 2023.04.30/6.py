inp = input('Введите строку: ')

set_inp = set(inp)
binary_set_nums = {'0', '1', 'b'}

if (
   not (set_inp <= binary_set_nums)
    # КОММЕНТАРИЙ: ох, накрутили проверок... есть такой эмпирический способ оптимизации кода: каждый раз когда у вас возникает третий подряд уровень вложенности условий (and — это те же вложенные условия), задавайте себе вопрос: "точно-точно-точно нельзя проще?" — в 95–97% случаев окажется, что можно =)
    or inp.count('b') > 1
    or 'b' in inp and '1' in inp[:inp.index('b')]
    # эти проверки возможно лишние
    or 'b' in inp and len(inp) == 1
    or '0b' in inp and len(inp) == 2
):
    print('Нет')
else:
    print('Да')

# ИСПОЛЬЗОВАТЬ: пожалуй, я просто оставлю здесь более короткий вариант, а вы его сами осмыслите и прокомментируйте основные действия во время работы над ошибками:
answer = 'нет'
if set(inp[2:]) <= {'0', '1'}:
    if inp[:2] in {'01', '10', 'b1', 'b0', '0b', '11', '00', '1', '0'}:
        answer = 'да'
print(answer)


# Введите строку: 1b0101
# Нет

# СДЕЛАТЬ: необходимо проверять больше вариантов входных данных


# ИТОГ: хорошо, но можно лучше — 2/3
