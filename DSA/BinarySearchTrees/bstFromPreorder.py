

 
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder_ans(root):
    if root is None: return

    print(root.data, end = " ")
    preorder_ans(root.left)
    preorder_ans(root.right)

def bstpre(preorder, preorderindex,key,min1,max1,n):

    if preorderindex >= n : 
        return None
    
    root = None
    if (key>min1 and key<max1) :
        root = node(key)
        preorderindex += 1

        if preorderindex < n:
            root.left = bstpre(preorder, preorderindex, preorder[preorderindex],min1, key,n)

        if preorderindex < n:
            root.right = bstpre(preorder, preorderindex, preorder[preorderindex],key,max1,n)
        

    return root    


preorder = [10, 5, 1, 7, 40, 50]
n = len(preorder)
preorderindex = 0
min1 = -float("inf")
max1 = float("inf")
root1 = bstpre(preorder,preorderindex,preorder[0],min1,max1,n)
preorder_ans(root1)
