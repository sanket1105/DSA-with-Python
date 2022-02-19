 
def subarrays(arr):
     n = len(arr)
     for i in range(0,n): ## starting point
         for j in  range(i,n): ## ending point
            for k in range(i,j+1):
                print(arr[k],end=" ")
            print("")     

subarrays([-1,4,7,2])     