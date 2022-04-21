
nums = [1,2,3,4,5,6]

def search(nums,target,index):
    if index == len(nums):
        return False
    if nums[index]==target: return index
    else: 
        return search(nums,target,index+1)

print(search(nums,6,0))