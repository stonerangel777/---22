n = int(input("Въведете положително число n: "))

numbers = list(range(1, n + 1))

dictionary = {}

for i in range(n):
    dictionary[numbers[i]] = numbers[n - 1 - i]

print("Списък:", numbers)
print("Речник:", dictionary)