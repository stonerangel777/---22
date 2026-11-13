numbers = tuple(map(int, input("Въведете числа: ").split()))

total = sum(numbers)

average = total / len(numbers)

even = tuple(number for number in numbers if number % 2 == 0)

print("Кортеж:", numbers)
print("Сума:", total)
print("Средно аритметично:", average)
print("Четни числа:", even)