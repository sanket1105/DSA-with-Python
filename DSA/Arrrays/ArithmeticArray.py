
## number of elements in the subarray with same common difference between them

a = [10,8,6,4,2,10,11]
ans=2
dif = a[1] - a[0]
j = 2
curr = 2
n =len(a)
while j<n:
    diff = a[j] - a[j-1]
    if diff == dif:
        curr += 1
    else:
        dif = diff
        curr= 2
    ans = max(ans,curr)
    j+=1

print(ans)
