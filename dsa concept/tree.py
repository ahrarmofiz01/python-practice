class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=node(3)
a=node(1)
b=node(2)
root.left=a
root.right=b
print(root.data)