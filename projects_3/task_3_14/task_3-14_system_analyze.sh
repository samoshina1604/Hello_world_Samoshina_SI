#!/bin/bash

# Вывод ФС и процента (без заголовка)
df -h | awk 'NR > 1 {print $1, $5}'

# Проверка на > 90%
df | awk 'NR > 1 {
    gsub(/%/, "", $5)
    if ($5 > 90) print "WARNING: " $1 " > 90%"
}'


