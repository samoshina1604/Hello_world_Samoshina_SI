#!/bin/bash

# ===== ЧАСТЬ 1: Создание файлов циклом for =====
echo "=== Создаем файлы ==="

for i in {1..10}; do
    touch "test${i}.txt"
    echo "Создан файл: test${i}.txt"
done

echo ""
echo "Всего создано файлов: $(ls test*.txt | wc -l)"
echo ""

# ===== ЧАСТЬ 2: Удаление файлов циклом while =====
echo "=== Удаляем файлы в обратном порядке ==="

count=10
while [ $count -ge 1 ]; do
    rm "test${count}.txt"
    echo "Удален файл: test${count}.txt"
    count=$((count - 1))
done

echo ""
echo "Все файлы удалены."

