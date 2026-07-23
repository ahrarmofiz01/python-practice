currentblance=10000
password=1234
pin=int(input("enter your pin:"))
if pin==password:
    print("your password is correct")
else:
    print("wrong password")

balance=100000
creditammount=int(input("enter your ammount"))
if creditammount<=balance:
    print(balance-creditammount,"this is your ablable balance")
elif creditammount>balance:
    print("incuficent balance")