class myclass:
    x=5
p1=myclass
print(p1.x)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("ahrar",36)
print(p1.name)
print(p1.age)
class math:
    def __init__(self,add,mul):
        self.add=add
        self.mul=mul
m=math(2,2)
print(m.add)
