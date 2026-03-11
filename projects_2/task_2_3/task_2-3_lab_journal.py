researcher_data = input("\n\tВведите ФИО исследователя: ")
date = input("\tВведите дату исследования: ")
experiment_name = input("\tВведите название исследования: ")
output = input("\tВведите вывод по исследованию: ")

width = 58
content_width = width - 4
separator = "+" + "-" * (width - 2) + "+"

with open("C:/Users/Света/PyCharmMiscProject/journal.txt", "w", encoding="utf-8") as file:
    print(separator)
    file.write(separator + "\n")

    print("| Электронный лабораторный журнал".ljust(width - 1) + "|")
    file.write("| Электронный лабораторный журнал".ljust(width - 1) + "|\n")

    print(separator)
    file.write(separator + "\n")

    print(f"| ФИО исследователя: {researcher_data}".ljust(width - 1) + "|")
    file.write(f"| ФИО исследователя: {researcher_data}".ljust(width - 1) + "|\n")

    print(f"| Дата: {date}".ljust(width - 1) + "|")
    file.write(f"| Дата: {date}".ljust(width - 1) + "|\n")

    print(f"| Эксперимент: {experiment_name}".ljust(width - 1) + "|")
    file.write(f"| Эксперимент: {experiment_name}".ljust(width - 1) + "|\n")

    print(separator)
    file.write(separator + "\n")

    print("| Вывод:".ljust(width - 1) + "|")
    file.write("| Вывод:".ljust(width - 1) + "|\n")

    words = output.split()
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= content_width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            print(f"| {current_line.ljust(content_width)} |")
            file.write(f"| {current_line.ljust(content_width)} |\n")
            current_line = word
    if current_line:
        print(f"| {current_line.ljust(content_width)} |")
        file.write(f"| {current_line.ljust(content_width)} |\n")
    print(separator)
    file.write(separator + "\n")

print("\nДанные успешно сохранены в файл journal.txt")