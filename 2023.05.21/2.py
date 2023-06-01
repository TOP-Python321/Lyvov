def deck() -> 'generator':

    """
    Создаёт упорядоченную колоду карт.
    
    :return: Возвращает объект генератор.
    """
    
    
    card_deck = ['черви', 'бубны', 'пики', 'трефы']
    
    for suit in  card_deck:
        for n in range (2, 15):        
            yield (n, suit)
    
    
    
# print(list(deck())[::13])
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]