
## Divide and Conquer Recurrence Relation
## in this search  space is reduced by a factor
## in binary search, we are reducing the size of array by half everytime


arr1 = [1,2,3,4,5,6,7]


## if you find some function calls or variables that need to passed in future function calls
## put those variables in the argument call in the function

def binarysearch(arr1,start,end,target):
    
    ## base condition
    if start>end: return -1
    
    mid = int((start+ end)/2)

    if arr1[mid]>target :   ## element lie in left side of mid
        end = mid-1
        return binarysearch(arr1,start,end,target)

    elif arr1[mid]<target: ## element lie in right of mid
        start=mid+1
        return binarysearch(arr1,start,end,target)

    else :
        return mid       


   
print("target value presented at index number: ")
print(binarysearch(arr1,0,len(arr1)-1,4))
