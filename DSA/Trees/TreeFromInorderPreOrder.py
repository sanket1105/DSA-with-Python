## tree from preorder and inorder

## pre -> root left right
## inorder-> left root right 

class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value


def buildtree(preorder,inorder):

    if inorder:
        index = inorder.index(preorder.pop(0))
        root = node(inorder[index])

        root.left = buildtree(preorder,inorder[:index]) 
        root.right = buildtree(preorder,inorder[index+1:])  

        return root

def postorder(root): ## left right root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")


preorder = [1,2,4,3,5]
inorder = [4,2,1,5,3]

root = buildtree(preorder,inorder)
print(postorder(root))
