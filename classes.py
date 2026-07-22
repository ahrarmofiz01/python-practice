class name:
    def __init__(self,name):
        self.name=name
p1 =name("ahrar")
print(p1.name)
#A function is used to perform a specific task. A class is used to create objects that have both data (variables) and behavior (methods). Functions are defined with def, while classes are defined with class.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=int(age)
a1=student("ahrar",20)
print(a1.name)
print(a1.age)