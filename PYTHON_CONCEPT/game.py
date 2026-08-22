atm_pin=2005
while True:
    pin=int(input("enter your pin:"))
    if pin==atm_pin:
        print("correct pin")
        break
    else:
        print("not correct")