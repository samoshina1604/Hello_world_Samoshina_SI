ph = float(input("Введите значение pH: "))

if ph == 7:
    print(f"pH = {ph} — это нейтральная среда")
elif ph < 7:
    print(f"pH = {ph} — это кислая среда")
else:  # ph > 7
    print(f"pH = {ph} — это щелочная среда")