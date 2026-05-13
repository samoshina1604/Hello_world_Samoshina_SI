numb = list(map(int, input("Введите числа через пробел: ").split()))

summ = 0
for num in numb:
    if num % 2 != 0:
        summ = summ + num

print(f"Сумма нечётных элементов: {summ}")