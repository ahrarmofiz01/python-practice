class node:
    def __init__(self,data):
        self .data=data
        self.next=None
a=node(1)
b=node(2)
c=node(3)
d=node(4)
head=a
a.next=b
b.next=c
c.next=d

def linkidl(head):
    curr=head
    while curr != None:
        print(curr.data)
        curr=curr.next
newnode=node(0)
curr=head
newnode.next=head
head=newnode
linkidl(head)


           

