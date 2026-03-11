# Вывод заголовка
print("=== Анализ последовательности ДНК ===\n")

# Принимаем ввод пользователя
dna_input = input("Введите последовательность ДНК: ")

# Приводим строку к верхнему регистру
dna_upper = dna_input.upper()
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")

# Считаем количество каждого нуклеотида
count_a = dna_upper.count('A')
count_t = dna_upper.count('T')
count_g = dna_upper.count('G')
count_c = dna_upper.count('C')

# Считаем общую длину строки
total_length = len(dna_upper)

# Вывод подсчета
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}")

print(f"\nОбщая длина: {total_length} нуклеотидов")

# Вывод процентного содержания
if total_length > 0:
    print("\nПроцентное содержание:")
    print(f"A: {(count_a / total_length) * 100:.2f}%")
    print(f"T: {(count_t / total_length) * 100:.2f}%")
    print(f"G: {(count_g / total_length) * 100:.2f}%")
    print(f"C: {(count_c / total_length) * 100:.2f}%")