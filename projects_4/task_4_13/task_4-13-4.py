n = int(input("Введите число N: "))

sum = 0
for i in range(1, n + 1):
    sum = sum + i

print(f"Сумма первых {n} натуральных чисел = {sum}")