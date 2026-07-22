number1=int(input("enter your number:"))
number2=int(input("enter your number:"))
number3=int(input("enter your number:"))
if (number1 > number2 and number1 < number3) or (number1 < number2 and number1 > number3):
    print("number1 is 2nd largest:", number1)

elif (number2 > number1 and number2 < number3) or (number2 < number1 and number2 > number3):
    print("number2 is 2nd largest:", number2)

else:
    print("number3 is 2nd largest:", number3)