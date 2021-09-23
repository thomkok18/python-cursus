def fibonacci(number):
    if (number == 1 or number == 2):
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

for i in range(1, 15):
    number = fibonacci(i)
    print(number)