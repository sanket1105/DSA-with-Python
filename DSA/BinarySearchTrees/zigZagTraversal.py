

## left to right, then right to left, then left to right and so on

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def zigzag(root):
    currlevel, nextlevel = [],[]
    lefttoright = True
    currlevel.append(root)
    

        