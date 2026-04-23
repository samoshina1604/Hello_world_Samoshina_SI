#!/bin/bash

echo "=== Работа с файлом data.csv ==="
echo ""

# 1. Вывод названий товаров (второе поле)
echo "1. Названия товаров:"
awk -F',' '{print $2}' data.csv

echo ""

# 2. Товары дороже 20 (третье поле > 20)
echo "2. Товары дороже 20:"
awk -F',' '$3 > 20 {print $2, "-", $3}' data.csv

echo ""

# 3. Общая стоимость (сумма всех цен)
echo "3. Общая стоимость всех товаров:"
total=$(awk -F',' '{sum += $3} END {print sum}' data.csv)
echo "   Итого: $total"

