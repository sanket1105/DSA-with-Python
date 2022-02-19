
a = [10,7,4,6,8,10,11]
n = len(a)
ans = 2
pd = a[1] - a[0]
curr = 2  ## current lenght of subarray
j = 2
     
while j<n:
    if pd == (a[j] - a[j-1]):
        curr+=1
    else:
        pd = a[j] - a[j-1]
        curr = 2 ## since string got break

    ans = max(ans,curr)   
    j+=1 

print(ans)



