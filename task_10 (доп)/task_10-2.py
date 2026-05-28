def parse_config(text):
    config_dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            config_dict[key.strip()] = value.strip()
    return config_dict


if __name__ == "__main__":
    config_text = """
    # Это комментарий
    temperature=37.5
    pH=7.2
    name=bioreactor_v1
    formula=a+b+c
    """
    result = parse_config(config_text)
    print("Результат работы функции:")
    print(result)