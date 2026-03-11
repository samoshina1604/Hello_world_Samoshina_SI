proteins = float(input("Масса белков (г): "))
fats = float(input("Масса жиров (г): "))
carbohydrates = float(input("Масса углеводов (г): "))

calories = (proteins * 4) + (fats * 9) + (carbohydrates * 4)
print(f"Общая калорийность: {calories} ккал")