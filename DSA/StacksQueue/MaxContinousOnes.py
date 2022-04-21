
'''
array given of 0 and 1
you change upto k values from 0 to 1 
length of longest subarray that contains only 1s
'''
k = 2
nums = [1,1,1,0,0,0,1,1,1,1,0]
n,end,start = len(nums),0,0
ans = 0

while end<n:
    if nums[end]==0:
        if k>0:
            k-=1
        else:
            ans = max(ans,end-start)
            if nums[start]==0:
                k+=1

            start+=1
            continue
    end+=1

ans = max(ans,end-start)
print(ans)
        