class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def LCA(root,n1,n2):
    if root==None: return None
    if root.val == n1 or root.val==n2: return root

    lt = LCA(root.left,n1,n2)
    rt = LCA(root.right,n1,n2)

    if lt and rt: return root
    if not lt and rt: return LCA(root.right,n1,n2)
    if lt and not rt: return LCA(root.left,n1,n2)
    else: return None 

def distance(root,n):
    if root==None: return -1
    if root.val == n: return 0

    lt = distance(root.left,n)
    rt = distance(root.right,n)
    dis = max(lt,rt)
    return dis+1 if dis>=0 else -1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

lca = LCA(root,1,5)
k1 = distance(lca,1)
k2=  distance(lca,5)
print(k1+k2)

