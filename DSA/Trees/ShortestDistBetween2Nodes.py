
## Shortest distance is the minimum number of edges to be traversed to reach one node to another node
## first find the LCA and then the distance between them


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def lca(root,n1,n2):
    if root == None: return None
    if root.data == n1 or root.data == n2 : 
        return root
    ld = lca(root.left,n1,n2) 
    rd = lca(root.right,n1,n2)

    if ld==None and rd==None: return None
    if ld!=None and rd==None: return ld
    if ld==None and rd!=None: return rd
    else: return root


def distances(root,n1):
    if root==None: return -1
    if root.data == n1: return 0


    lh = distances(root.left,n1)
    rh = distances(root.right,n1)

    dis = max(lh,rh)
    if dis>=0: return dis+1
    else: return -1

def distance_nodes(root,n1,n2):
    Lca = lca(root,n1,n2)
    return distances(Lca,n1) + distances(Lca,n2)



print(distance_nodes(root,4,2))

