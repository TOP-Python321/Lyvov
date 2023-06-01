list_of = [
    {
        'Липецк': 1,
        'Пермь': 9,
        'Ростов-на-Дону': 6,
        'Тула': 3,
        'Ульяновск': 7,
        'Ярославль': 9
    },
    {
        'Барнаул': 5,
        'Краснодар': 9,
        'Красноярск': 9,
        'Махачкала': 5,
        'Новосибирск': 7,
        'Пермь': 3,
        'Ростов-на-Дону': 5,
        'Самара': 2,
        'Санкт-Петербург': 6,
        'Хабаровск': 7
    },
    {
        'Краснодар': 4,
        'Красноярск': 1,
        'Москва': 1,
        'Санкт-Петербург': 4,
        'Тольятти': 9,
        'Тула': 2,
        'Тюмень': 5,
        'Ульяновск': 4
    },
]
list_out = {}

for i in list_of:
    for k, v in i.items():
        if k in list_out:
            list_out[k] = list_out[k] | {v}
        else:
            list_out[k] = {v}

print(
    *{
        f'{repr(k)}: {v}'
        for k, v in list_out.items()
    },
    sep=',\n'
)


# 'Ульяновск': {4, 7},
# 'Хабаровск': {7},
# 'Тольятти': {9},
# 'Тула': {2, 3},
# 'Краснодар': {9, 4},
# 'Красноярск': {9, 1},
# 'Махачкала': {5},
# 'Ростов-на-Дону': {5, 6},
# 'Санкт-Петербург': {4, 6},
# 'Тюмень': {5},
# 'Ярославль': {9},
# 'Барнаул': {5},
# 'Новосибирск': {7},
# 'Липецк': {1},
# 'Самара': {2},
# 'Москва': {1},
# 'Пермь': {9, 3}


