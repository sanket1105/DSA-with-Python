
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def kthlevelsum(root,k):
    if root==None: return
    queue = []
    queue.append(root) ## appending root to queue
    sum = 0
    level = 0
    flag = 0
    while len(queue)!=0:
        
        size = len(queue) ## number of elements at current level
        while size!=0:
            size-=1
            ptr = queue[0]
            queue.pop(0)

            if level==k:
                sum+=ptr.val
                flag = 1

            else:
                if ptr.left: queue.append(ptr.left)
                if ptr.right: queue.append(ptr.right)

        level+=1
        if flag==1: break
    return sum        



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 
  
print(kthlevelsum(root,2))
