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
def linkedlist():
    a = node(10)
    b = node(20)
    c = node(30)

    a.next = b
    b.next = c

    head = a
    curr = head
    while curr:
        print(curr.data)
        curr=curr.next
    head=head.next
    curr=head
    newnode=node(100)
    newnode.next=curr
    curr=newnode
    while curr:
        print(curr.data)
        curr = curr.next
    curr=head
    prev=None
    while curr:
        nextnode=curr.next
        curr.next=prev
        prev=curr
        curr=nextnode
    

linkedlist()