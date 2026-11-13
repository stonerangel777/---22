numbers = list(map(int, input("Въведете числа: ").split()))

minimum = min(numbers)
maximum = max(numbers)

print("Най-малък елемент:", minimum)
print("Брой срещания:", numbers.count(minimum))

print("Най-голям елемент:", maximum)
print("Брой срещания:", numbers.count(maximum))