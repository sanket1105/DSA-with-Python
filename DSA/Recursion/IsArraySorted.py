
def arraySorted(arr,idx):

    if idx==len(arr)-1 or len(arr)==0: return True
    if arr[idx] < arr[idx+1]:
        return arraySorted(arr1,idx+1)
    else: return False    

 
arr1 = [1,2,3,4,7,6] 
if(arraySorted(arr1,0)) : print("sorted array")
else: print("Not sorted array")
