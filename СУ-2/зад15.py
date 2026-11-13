n = int(input("Въведете число n: "))

dictionary = {}

for i in range(1, n + 1):
    dictionary[i] = (i ** 2, i ** 3)

print("Полученият речник е:")
print(dictionary)