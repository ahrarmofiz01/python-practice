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
#insert at the first point
newnode=node(0)
newnode.next=head
#delete add the  first point
head=newnode
head=head.next

   
linkedl(head)

           

