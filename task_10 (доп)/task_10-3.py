import json

def analyze_process_logs(json_path, report_path):
    level_counts = {}
    total = 0

    with open(json_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                event = json.loads(line)
                level = event.get('level')
                if level:
                    level_counts[level] = level_counts.get(level, 0) + 1
                    total += 1

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("Process Log Report\n")
        f.write("===============\n")
        for level in sorted(level_counts.keys()):
            f.write(f"{level}: {level_counts[level]}\n")
        f.write(f"Total: {total}\n")

    return level_counts


if __name__ == "__main__":
    test_logs = [
        {'timestamp': "2024-01-01 10:00:00", 'level': "INFO", "message": "Heating started"},
        {'timestamp': "2024-01-01 10:05:00", 'level': "INFO", "message": "Temperature reached"},
        {'timestamp': "2024-01-01 10:10:00", 'level': "WARNING", "message": "High pressure"},
        {'timestamp': "2024-01-01 10:15:00", 'level': "INFO", "message": "Cooling started"},
        {'timestamp': "2024-01-01 10:20:00", 'level': "ERROR", "message": "Sensor failure"},
    ]

    with open('test_logs.json', 'w', encoding='utf-8') as f:
        for log in test_logs:
            f.write(json.dumps(log) + '\n')

    result = analyze_process_logs('test_logs.json', 'report.txt')
    print("Возвращаемый словарь:", result)
    print("\nОтчёт записан в файл report.txt")

    with open('report.txt', 'r', encoding='utf-8') as f:
        print("\n" + f.read())