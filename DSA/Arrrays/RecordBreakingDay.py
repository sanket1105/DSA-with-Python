
## presnt value largr than all the previous values
## or its a last value or greater than the following value
## first day can be a record breaking dat
a = [1,2,0,7,2,0,2,2]
rbd = 0
mx = -1
for i in  range(len(a)):

    if len(a) == 1:
        rbd = 1
        break

    if a[i] > mx and a[i]>a[i+1]:
        rbd+=1

    mx = max(mx,a[i])

print(rbd)        



