

## First missniing number
## array elements are from [0,n]

## first sort and see which is missing where i!=k[i]

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
        print(nums)
        print("")
        return n        

nums =[0,2,3]
print(firstMissing(nums))

print(firstMissing([0,1,2,3]))