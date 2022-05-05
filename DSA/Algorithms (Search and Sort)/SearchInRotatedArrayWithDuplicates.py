
## roated array with dupliactes 

nums = [2,5,6,0,0,1,2]
target = 8

start = 0
end = len(nums)-1
found = False

while start<=end:
    mid = (start+end)//2

    if nums[mid]==target:
        found = True
        print("Found")
        break

    if nums[mid] == nums[end]: ## doesn't know which side is sorted one
        end-= 1

    if nums[mid]>nums[end]:   ## if left side is sorted:
        if nums[mid] >= target and nums[start]<=target:
            end =  mid - 1
        else: 
            start = mid + 1 

    else:  ## right side is sorted:
        if nums[mid]<target and nums[end]>=target:
            start =  mid+1
        else: 
            end = mid-1


if found==False: print("Not found")
                   
