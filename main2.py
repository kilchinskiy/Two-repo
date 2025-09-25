#Modul 4 Home work 3

#Створив віртуальне оточення.Terminal-python -m venv venv.
#Активував його.Terminal-venv\Scripts\activate.
#Встановив colorama.Terminal-pip install colorama.

import sys #Шлях до папки.
from pathlib import Path #Робота з файлами/папками.
from colorama import Fore, Style, init #Робить кольоровий текст.


init(autoreset=True) #Налаштування для кольорів.

def print_tree(path: Path, indent: str = ""): #Рекурсивний спосіб
    if not path.exists():
        print(Fore.RED + f"Шлях '{path}' не існує!")
        return

    if not path.is_dir():
        print(Fore.RED + f"'{path}' не є директорією!")
        return

    print(Fore.BLUE + f"{path.name}/") #Вивід назви папки.

    for item in path.iterdir(): #Обхід вмісту директорії.
        if item.is_dir():
            print(indent + Fore.BLUE + f"{item.name}/")
            print_tree(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)

if __name__ == "__main__": #Основний файл для запуску.
    if len(sys.argv) > 1:
        dir_path = Path(sys.argv[1])
    else:
        dir_path = Path.cwd()

    print_tree(dir_path) #Поточна директорія де лежить файл hw03.py.