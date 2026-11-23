class student:
    def __init__(self,name,__marks):
        self.name=name
        self.__marks=__marks
    @property
    def marks(self):
        return self.__marks
s1=student("ahrar",100)
print(s1.marks)