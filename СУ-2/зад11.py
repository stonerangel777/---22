students = {
    "Иван": 5.50,
    "Мария": 6.00,
    "Петър": 4.00,
    "Георги": 4.75,
    "Елена": 5.00
}

total = 0

print("Студенти с оценка над 4.50:")

for name, grade in students.items():
    if grade > 4.50:
        print(name, "-", grade)

    total += grade

average = total / len(students)

print("Среден успех:", average)