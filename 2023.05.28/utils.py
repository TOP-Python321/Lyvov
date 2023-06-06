from pathlib import Path
import importlib.util
import re
import shutil

def important_message(text: str) -> str:

    """
    генерирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'.
    
    :param text: Сообщени от пользователя. Строка
    
    :return: Строку.
    """
    
    import shutil
    
    col, line = shutil.get_terminal_size()
    str_outer = f"#{'='*(col-3)}#\n"
    str_space = f"#{' '*(col-3)}#\n"
   
    content_text =''
    while len(text)>0:
        content_text += f"#{text[:col-7].center(col-3)}#\n"
        text = text[(col-7):]
    
    return str_outer + str_space + content_text + str_space + str_outer
    
    
def load_file(path: str):
    """
    Осуществляет копирование файла по переданному пути в основной каталог.
    
    :param path: Потеряный файл. Строка.
    
    :return: Возвращает объект модуля, созданного при импортировании файла.
    """
    user_path = Path(path)
    load_path = Path.cwd()

    shutil.copy2(user_path, load_path)
    
    name_modul = user_path.name
    path_modul = load_path.joinpath(name_modul)
    spec = importlib.util.spec_from_file_location(name_modul, path_modul)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module