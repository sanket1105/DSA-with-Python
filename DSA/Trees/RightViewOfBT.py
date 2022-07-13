from collections import deque

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def rightview(root):
    if root==None: return
    q = []
    q.append(root)

    while len(q)>0:
        n = len(q)
        while n>0:
            n-=1
            node = q.pop(0)
            if n==0:
                print(node.val, end=" ")
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)    

      

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)

rightview(root)



