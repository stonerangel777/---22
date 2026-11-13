products1 = {
    "Ябълки": 10,
    "Банани": 5,
    "Портокали": 8
}

products2 = {
    "Банани": 7,
    "Портокали": 4,
    "Круши": 6
}

result = products1.copy()

for product, quantity in products2.items():
    if product in result:
        result[product] += quantity
    else:
        result[product] = quantity

print("Обединен речник:", result)