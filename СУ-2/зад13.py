set1 = set(map(int, input("Въведете първото множество: ").split()))
set2 = set(map(int, input("Въведете второто множество: ").split()))

print("Обединение:", set1 | set2)

print("Сечение:", set1 & set2)

print("Разлика:", set1 - set2)

print("Симетрична разлика:", set1 ^ set2)