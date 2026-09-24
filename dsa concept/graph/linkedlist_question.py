class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
head=a
def linkedl(head):
    curr=head
    while curr != None:
        print(curr.data)
        curr=curr.next
a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
head=a
newnode=node(0)
newnode.next=head
head=newnode
#insert at endnode
newnode=node(5)
curr=head
while curr.next !=None:
    curr=curr.next
curr.next=newnode
#insert at k th term
k=4
curr =head
newnode=node(7)
for i in range(k-2):
    curr=curr.next
newnode.next=curr.next
curr.next=newnode


linkedl(head)

           

