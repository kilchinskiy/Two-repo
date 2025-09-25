#Modul 4 Home work 2
import os #Він надає функції для роботи з файлами, папками, шляхами та іншими системними ресурсами.


file_path = "cats.txt"#Дорога до файлу.


if not os.path.exists(file_path):#Вхідні данні.
    cats_lines = [
        "60b90c1c13067a15887e1ae1,Tayson,3",
        "60b90c2413067a15887e1ae2,Vika,1",
        "60b90c2e13067a15887e1ae3,Barsik,2",
        "60b90c3b13067a15887e1ae4,Simon,12",
        "60b90c4613067a15887e1ae5,Tessi,5"
    ]
    with open(file_path, "w", encoding="utf-8") as f:#Створення файлу.
        for line in cats_lines:
            f.write(line + "\n")


def get_cats_info(path):# Функція для читання та обробки даних про котів.
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()  #Видаляємо прогалини та перенесення рядка.
                if not line:
                    continue
                parts = line.split(",")#Розділяємо рядок на частини.
                if len(parts) != 3:
                    continue
                cat_id, name, age_str = parts
                try:
                    age = int(age_str) #Перетворимо вік на число.
                except ValueError:
                    continue
                cats.append({
                    "id": cat_id,#Формуємо словник з даними кота.
                    "name": name,
                    "age": age
                })
        return cats
    except FileNotFoundError:#Обробка помилки.
        print(f"Файл {path} не найден!")
        return []

#Перевірка.
cats_info = get_cats_info(file_path)
print(cats_info)