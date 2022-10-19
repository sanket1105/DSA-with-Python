k = [6,5,9,4,5,9,8,7]
n = len(k)

for i in range(n-1):
    for j in range(i+1,0,-1):
        if k[j] < k[j-1]:
            k[j],k[j-1] = k[j-1],k[j]
        else:
            break
print(k)            
