nums = [2,1,2,3,4]
i = 0
while i < len(nums):
    if nums[i] != i+1:
        correctIndex  = nums[i]-1
        if nums[i]!=nums[correctIndex]:
            nums[i],nums[correctIndex] = nums[correctIndex],nums[i]
        else:
            print(nums[i])
            break
    i+=1   


print(nums)