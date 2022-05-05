

arr = [4,5,6,7,0,1,2]

def pivot(arr):
    start = 0
    end = len(arr)-1

    while start<end:
        mid = (start+end)//2
        if mid<end and arr[mid]>arr[mid+1]:
            return mid
        if mid>start and arr[mid]<arr[mid-1]:
            return mid-1
        if arr[start]>=arr[mid]:
            end = mid-1
        else: 
            start = mid + 1     
    return -1     

pivot_ele = pivot(arr)
if pivot_ele==-1:
    print("0 rotations")
else: print(pivot_ele+1," rotations")    