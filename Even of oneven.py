inputNumber = input("Enter a number: ")
num = int(inputNumber)
mod = int(num % 2)
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")