

## binary tree: hierarchical Data Structure
## in general Tree: root node -> branches -> leaves

'''
In binary tree: max only 2 branches can go out

left child -> root(Parent node ) <- right child

nodes with same parent: siblings

leaf node: no new node is coming out of it
'''

## tree from preorder: Root -> Left -> Right
## inorder: Left -> Root -> right
## postorder : Left -> right -> Root
'''
-1 in preorder represents the null node
'''

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)    
root.left.right = Node(5)

