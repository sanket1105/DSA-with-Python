k = [1,2,3,2,5]
i = 0
while i< len(k):
    corrindex = k[i]-1
    if k[i]!= k[corrindex]:
        k[i],k[corrindex] = k[corrindex],k[i]
    else: i+=1
print(k)        

ans = []
for i in range(len(k)):
    if k[i]!=i+1:
        ans.append(k[i])
        ans.append(i+1)
print(ans) 