from pathlib import Path


def list_files(user_path: str) -> tuple | None:
    """
    Возвращает кортеж с именами файлов в каталоге по переданному пути.
    
    :param user_path: Абсолютный путь к каталогу в виде объекта str.
    :return: Возвращает кортеж с именами файлов или None.
    """
    path = Path(user_path)
    files = tuple((file.name if file.is_file() else None for file in path.glob('**/*')))
    
    return files
    
    
# print(list_files(r'C:\Users\Симба\Desktop\Development\Python\Lyvov\2023.05.28\data'))
# ('7MD9i.chm', None, 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', None, 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip', '5vsIh.dat', 'P2a91.dat', 'RoBjg.pt', 'z03EN.pt')