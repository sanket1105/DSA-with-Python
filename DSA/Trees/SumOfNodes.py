

class newNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def sumnodes(root):

    if root==None: return 0
    total = 0

    return root.val + sumnodes(root.left) + sumnodes(root.right)

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)

print(sumnodes(root))