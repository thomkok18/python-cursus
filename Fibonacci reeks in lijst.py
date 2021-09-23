def fibonacci(number):
    list = []
    number1, number2 = 0, 1
    while len(list) < number:
        number1, number2 = number2, number1 + number2
        list.append(number1)
    return list

print("Result: ", fibonacci(15))