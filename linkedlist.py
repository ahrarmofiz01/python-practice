#building a linked list
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
print(head.data)
#traverse.   
def linkedlist(head):
    newnode=node(4)
    curr=head
    while curr.next!= None:
        curr=curr.next
    curr.next=newnode
    return head
head=linkedlist(head)
curr=head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("none")


