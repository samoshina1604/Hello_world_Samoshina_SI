def process_samples(records: list[dict]) -> tuple[list[dict], list[str]]:
    """
    Обрабатывает список проб, конвертирует значение value в float,
    добавляет поле quality и разделяет корректные записи и ошибки.

    Аргументы:
        records: список словарей, каждый должен содержать ключи "id" и "value"

    Возвращает:
        Кортеж (processed_records, errors), где:
        - processed_records: список обработанных словарей с полями id, value, quality
        - errors: список строк ошибок в формате "Sample <id>: <error_message>"
    """
    processed_records = []
    errors = []

    for record in records:
        sample_id = record.get("id")
        value_str = record.get("value")

        if sample_id is None:
            errors.append("Sample unknown: missing 'id' field")
            continue
        if value_str is None:
            errors.append(f"Sample {sample_id}: missing 'value' field")
            continue

        try:
            value = float(value_str)
        except ValueError as e:
            errors.append(f"Sample {sample_id}: invalid float value '{value_str}' - {e}")
            continue
        except TypeError:
            errors.append(f"Sample {sample_id}: value is not a string or number - {value_str}")
            continue

        if value < 5:
            quality = "low"
        elif value <= 10:
            quality = "normal"
        else:
            quality = "high"

        processed_record = record.copy()
        processed_record["value"] = value
        processed_record["quality"] = quality
        processed_records.append(processed_record)

    return processed_records, errors


if __name__ == "__main__":
    test_data = [
        {"id": "S1", "value": "4.2"},
        {"id": "S2", "value": "7.5"},
        {"id": "S3", "value": "12.0"},
        {"id": "S4", "value": "abc"},
        {"id": "S5"},
        {"value": "9.0"},
    ]

    processed, errors = process_samples(test_data)

    print("Обработанные записи:")
    for p in processed:
        print(p)

    print("\nОшибки:")
    for e in errors:
        print(e)