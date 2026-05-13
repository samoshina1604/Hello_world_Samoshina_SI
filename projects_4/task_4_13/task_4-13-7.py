numb = list(map(int, input("Введите числа через пробел: ").split()))

ave = sum(numb) / len(numb)
print(f"Среднее арифметическое: {ave}")