numb = list(map(int, input("Введите числа через пробел: ").split()))

summ = 0
for num in numb:
    if num > 0:
        summ = summ + 1

print(f"Количество положительных чисел: {summ}")