#linkedlist.py
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(2)
c=node(3)
head=a
a.next=b
b.next=c

print(head.next.next.data)