number = input("Въведете цяло число: ")

tuple1 = tuple(number)
tuple2 = tuple(number[::-1])

print("Цифри в прав ред:", tuple1)
print("Цифри в обратен ред:", tuple2)