
## in this you don't know whether the sorted array will be given in asceding or descending order


arr =[9,8,7,6,5,4,3,2,1]

target = 1
start = 0
end = len(arr)-1

k = arr[start] < arr[end]
## k will be 1 if in ascending order else k=0

while start<=end:
    mid = start + (end-start)//2

    if arr[mid] == target: 
        print("target at ", mid)
        ans = True
        break;

    if k:  ## if ascending
        if arr[mid] > target: 
            end = mid -1
        else: start = mid + 1

    else: ## descending
        if arr[mid] > target: 
            start = mid+1
        else: end = mid - 1   

if ans==False: print(" no such element in array")






