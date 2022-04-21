
## infinite arrays
## it means you don't know the size of the array

def binary_search(k,start,end,target):
    while start<=end:
        mid = (start+end)//2

        if k[mid] == target:
            return mid

        elif k[mid] > target:
            end = mid - 1
        else:
            start = mid + 1            

    return -1


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170,185]
target = 185

low,high = 0,1

while (target>arr[high]):
    newlow=high
    high = (high-low+1)*2
    low = newlow

ans = binary_search(arr,low,high,target)

if ans==-1:
    print("Not found")
else: print("found at: ",ans)    