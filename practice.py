name=input("enter student name:")
marks=[80,90,87,78]
print(sum(marks)/4)
average=sum(marks)/4
if average > 80 :
    print(name,"nice you are eligble")
else:
    print("better luck next time")

add1 = input("Enter fruit 1: ")
add2 = input("Enter fruit 2: ")
add3 = input("Enter fruit 3: ")
add4 = input("Enter fruit 4: ")

fruits = ["apple", "banana", "orange", "kiwi"]

user_list = [add1, add2, add3, add4]

if user_list == fruits:
    print("Correct! The lists are the same.")
else:
    print("Wrong! The lists are not the same.")