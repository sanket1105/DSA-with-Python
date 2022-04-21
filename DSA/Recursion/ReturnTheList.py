

## Return the list without providing it in the argument of the recursion function

nums =[1,2,3,4,4,5]

def search(nums,target,index):
    k = list()

    if index==len(nums):
        return k

    if nums[index]==target:
        k.append(index)

    
    callsFromBelow = search(nums,target,index+1)

    k.extend(callsFromBelow)

    return k

print(search(nums,4,0))