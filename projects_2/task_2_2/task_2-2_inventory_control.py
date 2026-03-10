# Запрос названия реактива
reagent_name = input("Введите название реактива: ")

# Запрос количества реактива
reagent_quantity = int(input("Введите количество реактива: "))

# Вывод отчета в консоль
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)

# Запись отчета в файл inventory.txt
with open("C:/Users/Света/PyCharmMiscProject/inventory.txt", "w", encoding="utf-8") as file:
 file.write(report)