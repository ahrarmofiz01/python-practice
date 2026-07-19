number1 = int(input("Enter your number1: "))
number2 = int(input("Enter your number2: "))
number3 = int(input("Enter your number3: "))

if number1 > number2 and number1 > number3:
    print(number1, "is the largest number")
elif number2 > number1 and number2 > number3:
    print(number2, "is the largest number")
else:
    print(number3, "is the largest number")


    