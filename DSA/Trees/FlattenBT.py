
## flatten in linked list: such that left of each node should point to null
## right should contain next node in preorder sequence
## not allowed to use any other data structures
## that is do everything in the tree only

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def flatten(root):
    

      if root==None or (root.left ==None and root.right==None): return  

      if root.left !=None:
        flatten(root.left)

      temp = root.right 
      root.right = root.left 
      root.left = None

      while root.right!=None:
        root = root.right
      root.right = temp  

      flatten(root.right)

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

flatten(root)
inorder(root)





