

## full nodes are those nodes which have both children as not null

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val



def fullnodes(root):
    if root == None:
        return

    queue = []
    queue.append(root)

    total = 0
    while len(queue)>0:

        node = queue.pop(0)

        if node.left is not None and node.right is not None:
            total+=1

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:    
            queue.append(node.right)    

    print("Total full nodes: ", total)    


## recursive approach
def countnodes(root):
 
    if (root == None):
        return 0
     
    res = 0
    if (root.left and root.right):
        res += 1
     
    res += (countnodes(root.left) +
            countnodes(root.right))

    return res
 

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

fullnodes(root)

print("Total full nodes are: ", end=" ")        
print(countnodes(root))
            
