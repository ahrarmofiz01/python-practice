number = int(input("Enter first number: "))
number1 = int(input("Enter second number: "))
number2 = int(input("Enter third number: "))

if (number > number1 and number < number2) or (number < number1 and number > number2):
    print("Second largest:", number)

elif (number1 > number and number1 < number2) or (number1 < number and number1 > number2):
    print("Second largest:", number1)

else:
    print("Second largest:", number2)