#Modul 4 Home work 1

import os #Він надає функції для роботи з файлами, папками, шляхами та іншими системними ресурсами.

file_path = "salaries.txt"#Дорога до файлу.

if not os.path.exists(file_path):#Вхідні данні.
    salary_lines = [
        "Alex Korp,3000",
        "Nikita Borisenko,2000",
        "Sitarama Raju,1000"
    ]
    with open(file_path, "w", encoding="utf-8") as f:#Створення файлу.
        for line in salary_lines:
            f.write(line + "\n")

def total_salary(path):#Підрахунок ЗП.
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()#Видаляємо прогалини та переноси рядків на початку та наприкінці.
                if not line:
                    continue
                parts = line.split(',')#Розділяємо рядок за комою.
                if len(parts) != 2:
                    continue
                name, salary_str = parts[0].strip(), parts[1].strip()
                try:
                    salary = float(salary_str)#Перетворення зарплати на число та підрахунок.
                except ValueError:
                    continue
                total += salary
                count += 1

        if count == 0:#Обчислення середньої зарплати.
            return (0, 0)
        average = total / count
        return (total, average)
    except FileNotFoundError:
        print(f"Файл {path} не найден!")
        return (0, 0)


#Перевірка
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
