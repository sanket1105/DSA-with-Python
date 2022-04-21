
nums = [1,2,3,4,5,4]

def sortedarr(nums,index):
    if index == len(nums)-1:
        return True

    return nums[index]<nums[index+1] and sortedarr(nums,index+1)


print(sortedarr(nums,0))