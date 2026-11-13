numbers = list(map(int, input("Въведете числа: ").split()))

unique = set(numbers)

repeated = []

for number in numbers:
    if numbers.count(number) > 1 and number not in repeated:
        repeated.append(number)

print("Уникални числа:", unique)
print("Брой различни числа:", len(unique))
print("Числа, които се повтарят:", repeated)