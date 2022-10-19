

## given tree is valid or not

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isbst(root,min,max):

    if root==None:
        return True

    if min!=None and root.data <= min.data:
        return False

    if max!=None and root.data >= max.data:
        return False

    ## checking for left and right sub tree
    leftvalid = isbst(root.left, min, root)
    rightvalid = isbst(root.right, root, max)

    return leftvalid and rightvalid

root = node(2)
root.left = node(1)
root.right = node(3)

print(isbst(root,None, None))