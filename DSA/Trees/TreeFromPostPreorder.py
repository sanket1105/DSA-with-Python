
from venv import main


class node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None



def preorder(root):
    if root:
        preorder(root.left)
        print(root.data,end=" ")
        preorder(root.right)

postorder = [4,2,5,3,1]
inorder = [4,2,1,5,3]

root = buildtree(postorder,inorder)
preorder(root)







