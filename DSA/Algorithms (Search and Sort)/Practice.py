
## bubbe sort

a=[9,5,8,56,88,5]

for i in range(len(a)):
    swap=False
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            swap=True
            a[j-1],a[j] = a[j],a[j-1]
    if swap==False:
        break

print(a)
