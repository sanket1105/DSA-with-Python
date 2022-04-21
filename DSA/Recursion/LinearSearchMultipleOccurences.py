

nums =[1,2,3,3,4,5]

def search(nums,target,index,ans):
    if index==len(nums):
        return ans
    if nums[index]==target:
        ans.append(index)
        return search(nums,target,index+1,ans)
    else:
         return search(nums,target,index+1,ans)

print(search(nums,3,0,[]))
   