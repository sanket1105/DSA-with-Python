
'''
In this we will be using recursion.
Split the array in two halves, sort the first one, sort the second one and merge both the ans and sort
'''

## https://www.youtube.com/watch?v=iKGAgWdgoRk&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=30
## watch this lecture

## time complexity: 
'''
At each step, we are reducing the array in half till single element is remaining
So here, splits are 2^n: hence here time complexity is log(N) base 2 for each level and there are n levels of
therefore time complexity will be n*log(n)

Space complexity: O(N)
'''  

def merge(arr1,arr2):

    arr3 =[0]*(len(arr1) + len(arr2))
    i,j,k = 0,0,0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            arr3[k] = arr2[j]
            j+=1
        else:   
            arr3[k] = arr1[i]
            i+=1

        k+=1    

    ## if array isn't finished
    while i <  len(arr1):
        arr3[k] = arr1[i]
        i+=1
        k+=1 

    while j <  len(arr2):
        arr3[k] = arr2[j]
        j+=1
        k+=1    

    return arr3        


def mergesort(nums):

    if len(nums)==1: return nums

    mid = len(nums)//2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])

    return merge(left,right)

nums = [5,9,8,5,3,6,7,4]

print(mergesort(nums))    