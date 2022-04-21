

## it will be same as printing the pattern from top to bottom
'''
In bubble sort, we push the max element to the last by cont. swapping
So here also, we will just go on rducing the len of the array and
SEe the implementation, you will understand
'''

nums = [5,4,3,2,1,2,2,15]

def bubble(nums,i,j):
    if i==0:
        return

    if i > j:
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]

        bubble(nums,i,j+1)

    bubble(nums,i-1,j)

bubble(nums,len(nums)-1,0)
print(nums)