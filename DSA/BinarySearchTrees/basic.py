
## no duplicate nodes
## left side of the node must be strictly less then the nodes key
## right side of the node must be strictly greater then the nodes key
## subtree must also be a subtree

## build a bst tree form array

## insertion time in bst is O(logn)

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root,val):
    if root==None:  ## nothing to compare now
        return node(val)

    if val < root.data:
        root.left = insertBST(root.left,val)

    else:
        root.right = insertBST(root.right,val)   

    return root  

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)


## lets create a tree : 
arr = [5,1,3,4,2,7]
root = None
root = insertBST(root,arr[0])

for i in range(1,len(arr)):
    insertBST(root,arr[i])
 
inorder(root)