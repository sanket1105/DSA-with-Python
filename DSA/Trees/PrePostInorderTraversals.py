class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root): ## left root right
    if root:   
        inorder(root.left) 
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root): ## root left right
    if root:   
        print(root.val,end=" ")
        preorder(root.left) 
        preorder(root.right)

def postorder(root): ## left right root
    if root:   
        postorder(root.left) 
        postorder(root.right)
        print(root.val,end=" ")




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)    
root.left.right = Node(5)

print("Inorder: ")
inorder(root)

print("")
print("Preorder: ")
preorder(root)

print("")
print("Postorder: ")
postorder(root)