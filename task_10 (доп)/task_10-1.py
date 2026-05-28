products = [
    {"sku": "A1", "category": "flour", "expected": 100, "actual": 95},
    {"sku": "B2", "category": "sugar", "expected": 50, "actual": 50},
    {"sku": "C3", "category": "enzyme", "expected": 10, "actual": 12},
]

discrepancies = []
for product in products:
    if product["actual"] != product["expected"]:
        diff = product["actual"] - product["expected"]
        discrepancies.append((product["sku"], diff))

by_category = {}
for product in products:
    category = product["category"]
    sku = product["sku"]
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(sku)

print("Расхождения:", discrepancies)
print("По категориям:", by_category)