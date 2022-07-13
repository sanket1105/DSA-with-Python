
## rather than passig the height function, lets pass the height in the diamter function itself


class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Height:
    def __init(self):
        self.h = 0
        return 0

def diamter(root,height):

    lh = Height()
    rh = Height()

    if root==None:
        height.h = 0
        return 0

    ld = diamter(root.left, lh)
    rd = diamter(root.right, rh)

    height.h = max(lh.h,rh.h) + 1
    return max(lh.h + rh.h + 1, max(ld,rd))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(diamter(root,Height))
