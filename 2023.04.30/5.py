scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

text_inp = input(' Введите слово: ').upper().replace('Ё', 'Е')

scores_word = 0

print(sum(scores_word + k for i in text_inp for k, v in scores_letters.items() if i in v))

# Введите слово: синхрофазотрон
# 29