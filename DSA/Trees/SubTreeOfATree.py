

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def areidentical(root1,root2):
    if root1 is None and root2 is None: return True
    if root1 is None or root2 is None: return False

    return (root1.data==root2.data and areidentical(root1.left,root2.left)
     and areidentical(root1.right,root2.right))


def issubtree(T,S):
    if S is None: return True
    if T is None: return False

    ## check with the root Node

    if (areidentical(T,S)): return True

    return issubtree(T.right,S) or issubtree(T.left,S)       


T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)



S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

print(issubtree(T,S))