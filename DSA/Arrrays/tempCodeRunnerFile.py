k = [-1,0,1,2,-1,-4]
k.sort()

i = 0
n = len(k)
for i in range(n-1):
    j = i+1
    l = n-1
    while j < l:
        
        if (k[i] + k[j] + k[l] == 0):
            print(k[i],k[j],k[l])
            j+=1
            l-=1

        elif  (k[i] + k[j] + k[l]) > 0:
            l-=1
        else:
             j+=1 