n = int(input("Введите число N: "))

summ = 0
for i in range(1, n + 1):
    summ = summ + i ** 2

print(f"Сумма квадратов первых {n} чисел = {summ}")