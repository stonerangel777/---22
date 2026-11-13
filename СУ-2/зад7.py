numbers = list(map(int, input("Въведете числа: ").split()))

x = int(input("Въведете число x: "))

indexes = []

for i in range(len(numbers)):
    if numbers[i] == x:
        indexes.append(i)

if len(indexes) > 0:
    print("Индексите са:", indexes)
else:
    print("Числото не се среща в списъка!")