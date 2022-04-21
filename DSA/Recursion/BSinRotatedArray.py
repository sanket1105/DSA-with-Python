
nums =[5,6,7,8,9,1,2,3]

def search(nums,target,start,end):
    mid = (start+end)//2

    if start>end: return -1

    if nums[mid]==target: return mid

    if nums[start]<=nums[mid]: ## this part is sorted by
        if target>=nums[start] and target<=nums[mid]:
            return search(nums,target,start,mid-1)
        else: 
            return search(nums,target,mid+1,end)

    else:
        if target<=nums[end] and target>=nums[mid]:
            return search(nums,target,mid+1,end)
        
        return search(nums,target,start,mid-1)
    

print(search(nums,9,0,len(nums)-1))
       


