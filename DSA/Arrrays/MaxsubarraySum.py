 
def subarrays(arr):
     n = len(arr)
     ans = 0
     for i in range(0,n): ## starting point
         for j in  range(i,n): ## ending point
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            ans = max(ans,sum)   
     print(ans)        
                
subarrays([-2,-3,4,-1,-2,1,5,-3])  


## optimized solution for the same problem
## using kadanes algorithm
## it looks for mainly continous positive entries

def maxsubarraySum(arr,n):
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1,n):
        curr_max = max(arr[i],curr_max+arr[i])
        max_so_far = max(max_so_far,curr_max)


    return max_so_far

arr = [-2,-3,-4,-1,-2,-1,-5,-3]
n = len(arr)
print(maxsubarraySum(arr,n))     

arr = [-2,-3,4,-1,-2,1,5,-3]
print(maxsubarraySum(arr,n)) 


## kadanes fails if all the entries are negative only
def kadanes(arr):
    currsum = 0
    maxsum = float('-inf')

    for i in range(len(arr)):
        currsum += arr[i]
        if currsum <0:
            currsum = 0

        maxsum = max(maxsum,currsum)
    print(maxsum)   

kadanes([-2,-3,-4,-1,-2,-1,-5,-3])

