avlbal = 10000 
code = 1234 


pin = int(input("Enter your pin: ")) 

while True: 
    if pin == code: 
        
        withdraw = int(input("Enter your amount: ")) 
        
        if withdraw <= avlbal: 
            print("Collect your cash") 
            avlbal -= withdraw 
            break 
        else: 
            print("Insufficient balance") 
            break 
    else: 
        print("Incorrect pin")
        
        pin = int(input("Enter your pin: ")) 

            
    
    