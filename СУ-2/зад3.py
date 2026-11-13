text = input("Въведете текст: ")

dictionary = {}

for symbol in text:
    if symbol in dictionary:
        dictionary[symbol] += 1
    else:
        dictionary[symbol] = 1

print("Речник:", dictionary)