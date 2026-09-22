#LINKEDLIST
class node:
     def __init__(self,data):
          self.data=data
          self.next=None
a=node(5)
b=node(6)
c=node(7)
head=a

a.next=b
b.next=c
print(head.next.next.data)