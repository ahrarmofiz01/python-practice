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
def linkll(head):
    curr=head
    while curr !=None:
        print(curr.data)
        curr=curr.next
a=node(2)
b=node(3)
c=node(4)
a.next=b
b.next=c
head=a
linkll(head)
