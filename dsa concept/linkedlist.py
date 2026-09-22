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
def printll(head):
     curr=head
     while curr !=None:
          print(curr.data)
          curr=curr.next
a=node(5)
b=node(6)
c=node(7)
head=a

a.next=b
b.next=c
printll(head)