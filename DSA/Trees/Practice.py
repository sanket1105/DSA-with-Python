
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end= " ")
        inorder(root.right) 

def preorder(root): ## root left right
    if root:   
        print(root.data,end=" ")
        preorder(root.left) 
        preorder(root.right)

def postorder(root): ## left right root
    if root:   
        postorder(root.left) 
        postorder(root.right)
        print(root.data,end=" ")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)    
root.left.right = Node(5)

## print("Inorder: ")
## inorder(root)

####################################################################################################################

# question 02

preorder = [1,2,4,3,5]
inorder = [4,2,1,5,3]

def buildtree(preorder,inorder):
    if inorder:
        ele = inorder.index(preorder.pop(0))
        root = Node(inorder[ele])

        root.left = buildtree(preorder,inorder[:ele])
        root.right = buildtree(preorder,inorder[ele+1:])

        return root

##root = buildtree(preorder,inorder)
##postorder(root)

#############################################################################

## level order traversal
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

def level_order(root):
    if root==None: return
    q = []
    q.append(root)

    while len(q)>0:
        print(q[0].data, end =" ")
        node = q.pop(0)

        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return q    

## print(level_order(root))

########################################################################
## level order sum
def level_order_sum(root,k):
    sum = 0
    level = 0
    if root==None:
        return sum

    q = []
    q.append(root)
    q.append(None)

    while len(q) > 0:
        node = q.pop(0)
        if node!= None:  
            if level==k:  
                sum += node.data
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        elif len(q) > 0:
            q.append(None)
            level+=1     

    return sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

## print(level_order_sum(root,1))

##########################################################################
## sum and total count of nodes

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

def sum_tree(root):
    if root==None: return 0
    total = 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)

def total_nodes(root):
    if root == None: return 0

    return total_nodes(root.left) + total_nodes(root.right) + 1

## print(sum_tree(root))    
## print(total_nodes(root))

########################################################################################

## height of the tree

def height(root):
    if root==None: return 0
    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)   
## print(height(root))     

##############################################
## diamter of tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

def height(root):
    if root==None: return 0
    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) + 1

def diameter(root):
    if root==None: return 0

    ld = diameter(root.left)
    rd = diameter(root.right)

    lh = height(root.left)
    rh = height(root.right)
    diam = lh+rh+1

    return max(diam, max(ld,rd))

## print(diameter(root))

####################################################
## diameter of tree: optimized
class Height:
    def __init(self):
        self.h = 0
        return 0

def diamter(root,height):

    lh = Height()
    rh = Height()

    if root==None:
        height.h = 0
        return 0

    ld = diamter(root.left, lh)
    rd = diamter(root.right, rh)

    height.h = max(lh.h,rh.h) + 1
    return max(lh.h + rh.h + 1, max(ld,rd))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#print(diamter(root,Height))

#############################################
## sum replacement


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

## print(level_order(root))
def sum_replacement(root):
    if root == None: return 0
    sum_replacement(root.left)
    sum_replacement(root.right)

    if root.left:
        root.data += root.left.data
    if root.right: 
        root.data += root.right.data
    return root

sum_replacement(root)     
## print(level_order(root))     


################################################
## height balanced tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def height_balanced(root):

    if root==None: return True

    if(height_balanced(root.left) == False or height_balanced(root.right) == False): 
        return False

    lh = height(root.left)
    rh = height(root.right)
    if abs(lh-rh) <= 1: return True
    else: return False

## print(height_balanced(root))

############################################################################
## right view
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def right_view(root):
    if root==None: return

    q = []
    q.append(root)

    while len(q) > 0:
        n = len(q)
        while n > 0:
            n -= 1
            node = q.pop(0)
            if n==0:
                print(node.data, end= " ")

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
  

##print("right view")
##right_view(root)

################################################################
## left view
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def left_view(root):
    if root==None: return
    q = []
    q.append(root)

    while len(q)>0:
        n = len(q)
        while n >0:
            n-=1
            node = q.pop()
            if n==0:
                print(node.data, end = " ")

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

## left_view(root)

#################################################################################
## shortest distance between 2 nodes

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def lca(root,n1,n2):
    if root==None: return None

    if root.data == n1 or root.data==n2 :
        return root ## found the lca

    lh = lca(root.left,n1,n2)
    rh = lca(root.right,n1,n2)

    if lh==None and rh==None: return None ## no lca found
    if lh!=None and rh == None: return  lh
    if lh==None and rh!=None: return rh
    else: return root ## when both are not none

def distance(root,n1):
    if root==None: return -1
    if root.data == n1: return 0

    lh = distance(root.left,n1)
    rh = distance(root.right,n1)

    dis = max(lh,rh)
    if dis>=0: return dis+1
    else: return -1

def distance_nodes(root,n1,n2):
    Lca = lca(root,n1,n2)  
    return distance(Lca,n1) + distance(Lca,n2)
    
## print(distance_nodes(root,1,8))
##################################################################

## flatten binary tree:
    
root = Node(4)
root.left = Node(9)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end= " ")
        inorder(root.right)

def flatten(root):
    if root == None or root.left == None and root.right == None: 
        return ## no need to flatten, tree already flatten

    if root.left != None :
        flatten(root.left)

        temp = root.right
        root.right = root.left
        root.left = None

        t = root.right
        while t.right!=None:
            t = t.right
        t.right =  temp   

    flatten(root.right)

#flatten(root)
#inorder(root)

##########################################################
# print all nodes at distance k from the given node
root = Node(4)
root.left = Node(9)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)


def dfs(root):
    if root==None: return 0

    lh = dfs(root.left)
    rh = dfs(root.right)

    max_single = max(max(lh,rh) + root.data, root.data)
    max_top = max(max_single, lh+rh+root.data)
    dfs.maxi = max(dfs.maxi, max_top)
    return max_single

def maxpathsum(root):
    dfs.maxi = float("-inf")
    dfs(root)
    return dfs.maxi

print(maxpathsum(root))

#############################################################

















#######################################################################
## lowest common ancestor
root = Node(4)
root.left = Node(9)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)

def lca(root,n1,n2):
    if root==None: return

    if root.data==n1 or root.data==n2:
        return root

    lh = lca(root.left,n1,n2)
    rh = lca(root.right,n1,n2)

    if lh==None and rh==None: return None
    if lh!=None and rh == None: return  lh
    if lh==None and rh!=None: return rh
    if lh!=None and rh != None: return root

## print(lca(root,1,3).data)    
###########################################################################

## max path sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def maxpathsum(root):
    ans = float("-inf")
