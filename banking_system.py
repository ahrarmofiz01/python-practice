class account:
    def __init__(self,name,ammount):
        self.name=name
        self.ammount=ammount
    def credit(self,ammount_deposit):
        self.ammount+=ammount_deposit
        return self.ammount
        
a1=account("ahrar",10)
print(a1.credit(5000))
