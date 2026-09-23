class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)
a.next=b
b.next=c
c.next=d
d.next=e
head=a
#print(a.next.data)
def linkedl(head):
    curr=head
    while curr.next!=None:
        print(curr.data)
        curr=curr.next

a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)
a.next=b
b.next=c
c.next=d
d.next=e
head=a
linkedl(head)
def linkedl(head):
    curr=head
    l=0
    while curr!= None:
        curr=curr.next
        l=l+1
    curr=head
    for i in range(l//2):
        curr =curr.next
    return curr
middle_node = linkedl(head)
print(middle_node.data)

           

