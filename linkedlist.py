class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(10)
b=node(20)
c=node(30)
a.next=b
b.next=c
print(a.next.data)