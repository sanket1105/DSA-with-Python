

## in normal search tree : searching time O(n)
## since we will be goiing to each and every node there

## wheres as in bst : since left and right follow some convention
## therefore time complexity reduces to O(log(n))


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def searchinbst(root,val):
    if root==None or root.data == val:
        return root

    if val > root.data:
        return searchinbst(root.right,val)

    else:
        return searchinbst(root.left,val)



root = node(4)
root.left = node(2)
root.right = node(5)
root.left.left = node(1)
root.left.right = node(3)
root.right.right = node(6)

k = searchinbst(root,88)
if k==None: print("Not found")
else:print("Found")