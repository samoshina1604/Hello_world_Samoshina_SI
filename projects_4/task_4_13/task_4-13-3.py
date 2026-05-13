n = int(input("Введите число N: "))

fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(f"{n}! = {fact}")