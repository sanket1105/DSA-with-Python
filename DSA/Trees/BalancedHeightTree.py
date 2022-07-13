
## when is the tree height balanced?
## when the absolute diff btween the left and right subtree is less than 1

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def height(root):
    if root==None: return 0

    lh = height(root.left)
    rh = height(root.right)

    return max(lh,rh)+1

def heightbalanced(root):

    ## base condition

    if root==None: return True ## for leaf nodes

    if heightbalanced(root.left)==False: return False
    if heightbalanced(root.right)==False: return False

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh)<=1: return True
    else: return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(heightbalanced(root))