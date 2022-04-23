

## binary tree: hierarchical Data Structure
## in general Tree: root node -> branches -> leaves

'''
In binary tree: max only 2 branches can go out

left child -> root(Parent node ) <- right child

nodes with same parent: siblings

leaf node: no new node is coming out of it
'''


# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key


# create root
root = Node(1)
root.left	 = Node(2);
root.right	 = Node(3);
root.left.left = Node(4);


