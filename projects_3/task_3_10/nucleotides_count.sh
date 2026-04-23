#!/bin/bash

# Выводим заголовок таблицы
printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

# Перебираем все FASTA-файлы
for file in *.fasta; do
    
    # Пропускаем, если файлов *.fasta не найдено (шаблон не раскрылся)
    [ -e "$file" ] || continue
    
    # Пропускаем пустые файлы
    if [ ! -s "$file" ]; then
        continue
    fi
    
    # Исключаем строки заголовков (начинающиеся с >) и объединяем в одну строку
    sequence=$(grep -v "^>" "$file" | tr -d '\n')
    
    # Считаем количество каждого нуклеотида
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    
    # Выводим результат в таблицу
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
    
done

