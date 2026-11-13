list1 = list(map(int, input("Въведете първия списък: ").split()))
list2 = list(map(int, input("Въведете втория списък: ").split()))

result = []

for number in list1:
    if number in list2 and number not in result:
        result.append(number)

print("Общи елементи:", result)