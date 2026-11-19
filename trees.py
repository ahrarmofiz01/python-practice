class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.right=node(4)
print(root.left.data)