import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 20))

print("Първоначален списък:", numbers)

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Списък без повторения:", unique)