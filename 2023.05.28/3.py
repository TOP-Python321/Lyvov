from pathlib import Path
from utils import load_file


def ask_for_file():
    """
    Запрашивает у пользователя путь к потерянному файлу и копирует этот файл.
    
    :return: Возвращает объект модуля, созданного при импортировании файла.

    """
    while True:
        file_path = input(r"путь: ")
        if not Path(file_path).is_file():
            print("не существует файл по указанному пути")
        else:
            break
    return load_file(file_path)
    
    
# config_module = ask_for_file()
# print(config_module.defaults)
# путь: C:\Users\Симба\Desktop\Development\Python\Lyvov\2023.05.28\data\conf.py
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}

# путь: C:\Users\Симба\Desktop\Development\Python\Lyvov\2023.05.28\data\klkf.py
# не существует файл по указанному пути
