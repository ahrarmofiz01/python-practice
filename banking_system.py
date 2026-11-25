class account:
    def __init__(self,name,ammount):
        self.name=name
        self.ammount=ammount
    def credit(self,ammount_deposit):
        self.ammount+=ammount_deposit
        return self.ammount
    def debit(self,ammount_debit):
        if self.ammount<ammount_debit:
            return "Insufficient balance"
        self.ammount-=ammount_debit
        return self.ammount

       
        return self.ammount
        
a1=account("ahrar",1000)
print( a1.debit(5000))
