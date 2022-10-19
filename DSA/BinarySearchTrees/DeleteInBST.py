

## cases:
# leaf node -> no issues
## node with a single child -> replace with that child
## node with double child -> heres the issue
## so we need to find the inorder successor and replace the node with it
## and then delete the node
 
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)


def inorderSucc(root):

    ## plot the tree with the given values
    ## you will see that the inorder successor is the left node to the given node
    # whose left is none
    ## else write down the inorder sequence and select the next element to the node
    
    curr = root

    while curr.left is not None:
        curr = curr.left

    return curr    


def deletebst(root,val):
    if root==None: return root

    if val < root.data:
        root.left = deletebst(root.left,val)

    elif val > root.data:
        root.right = deletebst(root.right,val)  

    else:

        ## case 1
        if root.left == None:
            temp = root.right
            root = None
            return temp
        # case 2
        elif root.right == None:
            temp = root.left
            root = None
            return temp    
              
        ## case 3
        temp = inorderSucc(root.right)
        root.data = temp.data ## swap the values

        ## now delete the right side, so again call the function
        root.right = deletebst(root.right,temp.data)

    return root




root = node(4)
root.left = node(2)
root.right = node(5)
root.left.left = node(1)
root.left.right = node(3)
root.right.right = node(6)

root = deletebst(root,5)
inorder(root)

