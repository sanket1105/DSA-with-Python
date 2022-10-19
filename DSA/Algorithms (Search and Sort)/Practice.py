'''
## selection sort

k = [2,2,1,1,1,8,2,2]

for i in range(len(k)):
    min = i
    for j in range(i,len(k)):
        if k[j]<k[min]:
            min = j
    k[i],k[min] = k[min],k[i]

print(k)


## bubble sort
for i in range(len(k)):
    swap = False
    for j in range(1,len(k)-i):
        if k[j-1] > k[j]:
            k[j-1],k[j] = k[j],k[j-1]
            swap= True

    if swap==False:
        break

print(k)

## selection sort

for i in range(len(k)):
    min = i
    for j in range(i,len(k)):
        if k[j]<k[min]:
            min = j

    k[i],k[min] = k[min],k[i]

print(k)    

## insertion sort

for i in range(len(k)):
    for j in range(i,0,-1):
        if k[j] < k[j-1]:
            k[j],k[j-1] = k[j-1],k[j]
        else:
            break

print(k)


## cyclic sort:

i = 0
while i < len(k):
    if k[i] != i+1:
        k[i],k[i+1] = k[i+1],k[i]   
    else:
        i+=1
print(k)            

'''

def merge(first,last):
    i,j,k = 0,0,0
    ans = [0]*(len(first)+len(last))

    while i<len(first) and j<len(last):
        if first[i] > last[j]:
            ans[k] = last[j]
            j+=1

        else:
            ans[k] =  first[i]
            i+=1
        k+=1

    while i<len(first):
        ans[k] = first[i]
        i+=1
        k+=1

    while j<len(last):
        ans[k] = last[j]
        j+=1
        k+=1

    return ans                   



## merge sort

def mergesort(k):

    if len(k) == 1: return k
    mid = len(k)//2

    first = mergesort(k[:mid])
    last = mergesort(k[mid:])

    return merge(first,last)



k = [1,2,3,6,9,8,5,2,4,7,55]
print(mergesort(k))

## selection sort
k = [6,5,9,4,5,9,8,7]
n = len(k)

for i in range(n):
    min = i
    for j in range(i,n):
        if k[j] < k[min]:
            min = j
    k[i],k[min] = k[min], k[i]   

print(k)

## bubble sort
k = [6,5,9,4,5,9,8,7]
n = len(k)
for i in range(n):
    swap = False
    for j in range(1,n-i):
        if k[j-1] > k[j]:
            k[j-1],k[j] = k[j],k[j-1]
            swap = True
    if swap == False:
        break
print(k)         


## insertion sort
k = [6,5,9,4,5,9,8,7]
n = len(k)

for i in range(n-1):
    for j in range(i+1,0,-1):
        if k[j] < k[j-1]:
            k[j],k[j-1] = k[j-1],k[j]
        else:
            break
print(k)            






