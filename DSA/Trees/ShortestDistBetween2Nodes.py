
## Shortest distance is the minimum number of edges to be traversed to reach one node to another node
## first find the LCA and then the distance between them

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def LCA(root,n1,n2):
    if root==None: return None
    if root.val==n1 or root.val == n2:
        return root ## LCA Found

    lt = LCA(root.left,n1,n2)
    rt = LCA(root.right,n1,n2)

    if lt!=None and rt!=None: return root 
    if lt==None and rt==None: return None
    if lt!=None and rt==None: return LCA(root.left,n1,n2)
    else: return LCA(root.right,n1,n2)

def distance(root,n):
    if root==None: return -1
    if root.val == n: return 0

    lt = distance(root.left,n)
    rt = distance(root.right,n)
    dis = max(lt,rt)
    if dis>=0: return dis+1
    else: return -1

def distance_nodes(root,n1,n2):
    lca = LCA(root,n1,n2)  
    return distance(lca,n1) + distance(lca,n2)


 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(distance_nodes(root,4,8))

