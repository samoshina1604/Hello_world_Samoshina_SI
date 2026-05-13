n = int(input("Сколько чисел вы хотите ввести? "))
numb = []

for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numb.append(num)

maximum = max(numb)
print(f"Максимальное число: {maximum}")