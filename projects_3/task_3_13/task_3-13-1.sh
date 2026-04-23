#!/bin/bash

# Используем символ "|" как разделитель вместо "/"
# Это позволяет не экранировать слэши в путях
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php

echo "Замена выполнена. Проверьте файл settings.php"

