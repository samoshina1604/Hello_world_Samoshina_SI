numb = list(map(int, input("Введите числа через пробел: ").split()))

summ = 0
num = 0
for i in range(len(numb)):
    if i % 2 == 0:
        summ = summ + numb[i]
        num = num + 1

if num > 0:
    gag = summ/num
    print(f"Среднее арифметическое c чётными индексами: {gag}")
else:
    print("Нет элементов с чётными индексами")