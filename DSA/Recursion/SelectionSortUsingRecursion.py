
nums = [8,9,85,84,3,2,8,1,1,5]

def selectionsort(nums,rows,cols):
    if rows==len(nums): return
    min = rows
    for i in range(rows,len(nums)):
        if nums[i] < nums[min]:
            min = i
    nums[rows],nums[min] = nums[min],nums[rows]

    selectionsort(nums,rows+1,cols)      

selectionsort(nums,0,0)
print(nums)

