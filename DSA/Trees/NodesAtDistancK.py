
## print all nodes which are at distance k

## So intuition: nodes in the subtree and other in the ancestors noedes

class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.val= val

## case 1
def knodessubtree(root,k):
    if root==None or k<0:
        return

    if k==0:
        print(root.val,end=" ")
        return

    knodessubtree(root.left,k-1)
    knodessubtree(root.right,k-1)    

## case 2
def printnodes(root,target,k):
    if root==None: return -1

    if root==target:
        knodessubtree(root,k)
        return 0 ## distance return

     


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
