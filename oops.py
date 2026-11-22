class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def detail(self):
        print(f"name:{self.name}")
        print(f"roll:{self.roll}")
s1=student("ahrar",1)
s2=student("aman",2)
print(s1.name)
print(s1.roll)
s1.detail()
s1.detail()
#default parameter
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.name="jsw"
        self.location="mumbai"
e1=employee("ahrar",101)
print(e1.id)
#math calculation
class math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def substract(self):
        return self.a-self.b
# Private variable(__)
#use for not accessssing the valu
class bankaccount:
    def __init__(self,name,__balance):
        self.name=name
        self.__balance=__balance
b1=bankaccount("ahrar",10000)
b1.balance=20000
print(b1.__balance)


