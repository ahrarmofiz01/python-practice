atm_pin = 2005

while True:

    pin = int(input("Enter the PIN: "))

    if pin == atm_pin:
        print("PIN is correct")
        break
    else:
        print("PIN is incorrect")
