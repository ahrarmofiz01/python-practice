print("========== ATM ==========")
print("1. Banking")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:

    print("\n------ Banking ------")
    print("1. Generate PIN")
    print("2. Login")

    option = int(input("Enter your choice: "))

    if option == 1:

        name = input("Enter Your Name: ")
        account = input("Enter Account Number: ")
        mobile = input("Enter Mobile Number: ")

        pin = input("Create a 4-digit PIN: ")
        confirm = input("Confirm PIN: ")

        if pin == confirm:
            print("\nPIN Generated Successfully.")
            print("Your ATM PIN is:", pin)
        else:
            print("PIN does not match.")

    elif option == 2:

        saved_pin = "1234"   # Assume this is the stored PIN
        entered_pin = input("Enter ATM PIN: ")

        if entered_pin == saved_pin:
            print("Login Successful.")
        else:
            print("Wrong PIN.")

    else:
        print("Invalid Banking Option.")

elif choice == 2:
    print("Thank you for using ATM.")

else:
    print("Invalid Choice.")