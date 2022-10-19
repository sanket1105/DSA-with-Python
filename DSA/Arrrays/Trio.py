
## trio with sum 0  and all 3 different


nums = [-1,0,1,2,-1,-4]
nums.sort()
ans=set()
for i in range(len(nums)):
    j=i+1
    k=len(nums)-1
    while(j<k):
        summ=nums[i]+nums[j]+nums[k]
        if summ==0 : 
            ans.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
        elif summ<0:
            j+=1
        else:
            k-=1

print(list(ans))    
