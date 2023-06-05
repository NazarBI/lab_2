import os
while True:

    # Запишемо шлях
    file_path = input("Введіть шлях в якому знаходиться файл:")


    # Перевірка
    if not os.path.isfile(file_path):
        print("Файл не знайдено")
        print("Перевірте чи правильно вказаний шлях")
        continue

    # Відкриємо файл
    with open(file_path, 'r') as f:
        # Інцілізуємо
        line_count = 0
        empty_line_count = 0
        z_line_count = 0
        z_count = 0
        and_line_count = 0

        for line in f:
            line_count += 1

            # перевіримо чи порожній
            if line.strip() == '':
                empty_line_count += 1

            # перевіримо чи z присутня у рядку
            if 'z' in line:
                z_line_count += 1
                z_count += line.count('z')

            # Перевіримо чи є and
            if 'and' in line:
                and_line_count += 1

        # Друкуємо
        print(" total line: ", line_count)
        print(" empty lines: ", empty_line_count)
        print(" lines with 'z': ", z_line_count)
        print(" 'z' count:", z_count)
        print(" lines with 'and': ", and_line_count)

    # Зробимо перевірку ще раз за потребністю користувача
    response = input("Analyze the file again? (y/n): ")
    if response.lower() != 'y':
        break
