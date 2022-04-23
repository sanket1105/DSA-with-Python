

## trees BFS is Level Order Traversal
## we will use queue here, FIFO
## as we are changing level, we will go on adding the numbers in the queue
## before removing it, just append the queue with its left and right children


class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def levelorder(root):
    if root==None: return

    queue = []
    queue.append(root) ## appending root to queue
    
    while len(queue)>0:
        print(queue[0].val, end= " ") 
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)   

print("Level order traversal is: ")
levelorder(root)