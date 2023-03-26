k = [1,2,3,6,5,4]
i = 0
while i<len(k):
    correctindex = k[i]-1
    if k[i]!=k[correctindex]:
        k[i],k[correctindex] = k[correctindex],k[i]
    i+=1
print(k)  