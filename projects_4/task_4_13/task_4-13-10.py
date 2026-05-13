numb = list(map(int, input("Введите числа через пробел: ").split()))

summ = 0
for i in range(len(numb)):
    if i % 2 != 0:
        summ = summ + numb[i]

print(f"Сумма элементов с нечётными индексами: {summ}")