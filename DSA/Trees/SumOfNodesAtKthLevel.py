
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data


def levelorder(root):
    if root==None: return

    queue = []
    queue.append(root)
   

    while len(queue)>0:
        print(queue[0].val, end=" ")

        node = queue.pop(0)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)


def levelordersum(root,k):
    if root==None: return  ##sum not possible
    queue = []
    queue.append(root)
    queue.append(None)
    level = 0
    sum = 0

    while len(queue)>0:
        node = queue.pop(0)
        if node!=None:
            if level==k:
                sum += node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)    

        ## if node none but queue not empty
        elif len(queue)>0:
            queue.append(None)
            level+=1

    return sum



root = Node (1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(-1) 

(levelorder(root))
print(" ")
print(levelordersum(root,2))
  

