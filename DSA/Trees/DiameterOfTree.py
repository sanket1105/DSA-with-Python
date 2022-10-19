
## The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes

## this is the approach of O(N**2 )


class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def height(root):
    if root==None:
        return 0

    lh = height(root.left)
    rh = height(root.right) 
    return max(lh,rh) + 1 ## 1 for root

def diameter(root):
    if root == None: return 0
    ld = diameter(root.left)
    rd = diameter(root.right)
    
    d3 = height(root.left) + height(root.right) + 1

    return max(d3,max(ld,rd))

 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))

