#!/bin/bash

echo "=== Статистика оценок студентов ==="
echo ""

# 1. Сумма всех оценок
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "1. Сумма всех оценок: $sum"

# 2. Средняя оценка
average=$(awk '{sum += $2} END {print sum/NR}' students.txt)
echo "2. Средняя оценка: $average"

# 3. Максимальная оценка
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "3. Максимальная оценка: $max"

