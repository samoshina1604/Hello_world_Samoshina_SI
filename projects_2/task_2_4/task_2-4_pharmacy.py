# Запрос общего количества капсул
total_capsules = int(input("Введите общее количество произведенных капсул: "))

# Запрос вместимости одной упаковки
package_capacity = int(input("Введите количество капсул в одной упаковке: "))

# Расчет полных упаковок и остатка
full_packages = total_capsules // package_capacity
remainder = total_capsules % package_capacity

# Вывод отчета
print()
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t{remainder}")