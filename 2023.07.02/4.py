import csv
from pathlib import Path
from sys import path

class CountableNouns:
   
    """
    Предоставляет интерфейс для работы с файловой базой существительных
    """
   
    db_path: Path = Path(path[0]) / 'words.csv'
    words: dict[str, tuple[str, str]] = {}
            
    with open(db_path, "r", encoding='utf-8') as r_file:
        for row in csv.reader(r_file):
            row = tuple(row)
            words |= {row[0]: row[1:]}

  
    @classmethod
    def pick(cls, number: int, word: str) -> str:
       
        """
        Принимает в качестве аргументов число и существительное для согласования в единственном числе,
        возвращает согласованное с переданным числом существительное
        """
        
        if word not in cls.words:
            cls.words[word] = tuple()
            return word                 
        
        elif word in cls.words and cls.words[word]:        
            list_1= [2, 3, 4]
            list_2 = [0, 5, 6, 7, 8, 9]

            if 11 <= number % 100 <=14 or number % 10 in list_2:
                return cls.words[word][1]
            elif number % 10 in list_1:
                return cls.words[word][0]
            else:
                return word
        else:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word)
       
    @classmethod
    def save_words(cls, word1: str = None) -> None:
    
        """Запрашивает в stdin у пользователя два или три слова согласующихся с числительными,
        добавляет полученные значения в поле класса words
        и дописывает их в файл с базой существительных"""
       
        if word1 is None:
            word1 = input('введите слово, согласующееся с числительным "один": ')  
            
        word2: str = input(' введите слово, согласующееся с числительным "два": ')
        word3: str = input(' введите слово, согласующееся с числительным "пять": ')
        
        cls.words[word1] = tuple([word2, word3])  

        with open(cls.db_path, 'w', encoding='utf-8') as w_file:
            row = csv.writer(w_file, delimiter = ",", lineterminator='\n')
            row.writerows([k, *v] for k, v in cls.words.items())
          
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(12,'год')
# 'лет'
# >>> CountableNouns.pick(1,'год')
# 'год'
# >>> CountableNouns.pick(22,'год')
# 'года'
# >>> CountableNouns.pick(3,'месяц')
# 'месяца'
# >>> CountableNouns.pick(16,'месяц')
# 'месяцев'
# >>> CountableNouns.pick(16,'день')
# 'дней'
# >>> CountableNouns.pick(1,'день')
# 'день'
# >>> CountableNouns.pick(11,'банан')
# 'банан'
# >>> CountableNouns.pick(11,'банан')
# существительное "банан" отсутствует в базе
 # введите слово, согласующееся с числительным "два": банана
 # введите слово, согласующееся с числительным "пять": бананов
# >>> CountableNouns.pick(11,'банан')
# 'бананов'
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": стол
 # введите слово, согласующееся с числительным "два": стола
 # введите слово, согласующееся с числительным "пять": столов
# >>> CountableNouns.pick(11,'стол')
# 'столов'
# >>> CountableNouns.pick(2,'стол')
# 'стола'
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# банан,банана,бананов
# стол,стола,столов

# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'банан': ('банана', 'бананов'), 'стол': ('стола', 'столов')}
# >>>