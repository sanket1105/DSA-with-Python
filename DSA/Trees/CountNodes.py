
## counting all nodes

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def countnodes(root):

    if root == None: return 0

    return 1 + countnodes(root.left) + countnodes(root.right)


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

print(countnodes(root))
