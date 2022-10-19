 

 ## selection sort
'''
## Select the min element is put at at its correct place thats is its correct index

We will go on selecting the min element and will put that element in the right spot

Best and worst case complecity is O(n^2).
## since we will have to find the min element

It is not stable algorithm


Use: performs well on small lists
 '''

k = [6,5,9,4,5,9,8,7]

for i in range(len(k)):
    min=i
    for j in range(i,len(k)):
        if k[j] < k[min]:
            min = j

    k[i],k[min] = k[min],k[i]        


print(k)

    