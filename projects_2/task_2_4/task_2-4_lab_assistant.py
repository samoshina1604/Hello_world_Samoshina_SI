# Запрос нужного объема раствора
volume = float(input("Введите нужный объем раствора (в мл): "))

# Расчет массы соли для 0.9% концентрации
salt_mass = volume * 0.009

# Объем воды (примерно равен общему объему)
water_volume = volume

# Запись рецепта в файл
with open("C:/Users/Света/PyCharmMiscProject/recipe_2.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {round(salt_mass, 2)} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")

print("Рецепт сохранен в файл recipe_2.txt")