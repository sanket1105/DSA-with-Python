
## theres a single element that is repeating in the array 
## find that duplicate

## values are between [1,n]

## we will use cycle sort, in this if any of the element is repeating, it will thrown to last
## see this by using pen and paper

## because the duplicate willl be thrown to the last 
## and when it will check for the cycle sort condition, its value is already there at its required index
## so it will just increment the i value when dealing with the duplicate element

## rather than returning the last element:
## if you find arr[i] != i+1, then swap if not equal else return that value
## thats the duplicate value

nums = [2,1,2,3]

i=0

i = 0
while i < len(nums):
    if nums[i] != i+1:
        correctIndex  = nums[i]-1
        if nums[i]!=nums[correctIndex]:
            nums[i],nums[correctIndex] = nums[correctIndex],nums[i]
        else:
            print(nums[i])
            break
    else: i+=1   


print(nums)
