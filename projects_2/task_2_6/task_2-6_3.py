# Получение групп крови донора и пациента
donor = input("Группа крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Группа крови пациента (I, II, III, IV): ").strip().upper()

# Проверка возможности переливания
if donor == "I" or donor == recipient:
    print(f"Переливание возможно: кровь группы {donor} совместима с группой {recipient}")
else:
    print(f"Переливание невозможно: кровь группы {donor} несовместима с группой {recipient}")