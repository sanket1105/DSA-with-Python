

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def height(root):
    if root==None: return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height:
            return left_height+1  ## 1 for root node
        else:
            return right_height+1  ## 1 for root Node   

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)         

print(height(root))