current_balance=10000
password=4321
pin=int(input("enter the pin"))
if password==pin:
    creditammount=int(input("enter the amount you want:"))
    if current_balance>=creditammount:
        print("your current balance",current_balance-creditammount)
    else:
        print("enter correct ammount")
