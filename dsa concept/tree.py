class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=node(6)
a=node(2)
b=node(3)
root.left=a
root.right=b
print(root.data)