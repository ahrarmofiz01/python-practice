#LINKEDLIST
class node:
     def __init__(self,data):
          self.data=data
          self.next=None
a=node(5)
b=node(6)
c=node(7)
d=node(8)
e=node(9)
f=node(10)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
head=a
print(head.next.next.data)