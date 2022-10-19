

## build balanced bst from the sorted array


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def preorder(root):
    if root:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)


def balancedtree(arr,start,end):
    
    if start>end : return None

    mid = (start+end)//2
    root = node(arr[mid])
    root.left = balancedtree(arr, start,mid-1)
    root.right = balancedtree(arr,mid+1,end)

    return root

arr = [10,20,30,40,50]
root = balancedtree(arr,0,len(arr)-1)
preorder(root)
