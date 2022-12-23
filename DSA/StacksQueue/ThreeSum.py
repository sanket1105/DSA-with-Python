

''''
Find if 3 numbers exits whose sum is equal to given value.
'''

a = [1, 4, 45, 6, 10, 8]
sum = 22
n = len(a)
 
a.sort()
found = False
for i in range(n-2):
    l = i+1
    r = n-1
    while l<r:
        if a[i] + a[l] + a[r] == sum:
            print("Triplet is : ", a[i],', ', a[l], ', ', a[r])
            found = True
            break

        elif a[i] + a[l] + a[r] < sum:
            l+=1
        else:
            r-=1  

if found==False:
    print("triplet not found")
