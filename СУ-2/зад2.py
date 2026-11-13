import random

numbers = []

for i in range(5):
    numbers.append(random.randint(1, 20))

print("Първоначален списък:", numbers)

result = []

for i in range(len(numbers) - 1):
    result.append(numbers[i])
    result.append(numbers[i] + numbers[i + 1])

result.append(numbers[-1])

print("Нов списък:", result)