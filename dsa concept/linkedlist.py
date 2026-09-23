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
#inset at the begining
newnode=node(8)
newnode.next=head
head=newnode
#insert at the end
newnode=node(9)
curr=head
while curr .next!=None:
    curr=curr.next
curr.next=newnode
#remove the first node
head=head.next
#remove the last node
curr=head
while curr.next.next!=None:
    curr=curr.next
curr.next=None
#insert add the kth indec
newnode=node(15)
k=3
curr=head
for i in range(k-2):
    curr=curr.next
newnode.next=curr.next
curr.next=newnode
#remove from kth index
k=3
curr=head
for i in range(k-2):
    curr=curr.next
curr.next=curr.next.next

linkll(head)
