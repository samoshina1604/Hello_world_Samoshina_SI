# Запрос данных
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")

# Создание файла и запись данных
with open("C:/Users/Света/PyCharmMiscProject/recipe.txt", "w", encoding="utf-8") as file:
    # Название среды — заголовок
    file.write(medium_name + "\n")
    # Параметры — списком ниже
    file.write(f"Концентрация агара: {agar_concentration}%\n")
    file.write(f"Температура стерилизации: {sterilization_temperature}°C\n")

# Вывод сообщения об успешном завершении
print("Файл 'recipe.txt' успешно сформирован!")