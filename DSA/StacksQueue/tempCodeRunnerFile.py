nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
start,end,n = 0,0,len(nums)
zerocount = 0
ans=  0

while end < n:
    if nums[end]==0:
        zerocount += 1

    while zerocount > k:
        if nums[start]==0:
            zerocount -= 1
        start += 1

    ans = max(ans,end-start+1)
    end+=1
print(ans) 