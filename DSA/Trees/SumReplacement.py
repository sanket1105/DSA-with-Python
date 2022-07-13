class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def sumreplacement(root):
    if root==None: return

    sumreplacement(root.left)
    sumreplacement(root.right)

    if root.left:
        root.val += root.left.val

    if root.right:
        root.val += root.right.val    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
print("")
sumreplacement(root)
inorder(root)

