

## First missniing number
## array elements are from [0,n]

def firstMissing(nums):
        i = 0
        n = len(nums)
        while i<n:
            if(nums[i]<n and nums[i]!=i):
                j = nums[i]
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i+=1
       
        for i in range(n):
            if i!=nums[i]:
                return i

        return n        

nums =[3,0,1]
print(firstMissing(nums))

print(firstMissing([0,1,2,3]))