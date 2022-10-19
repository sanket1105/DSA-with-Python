

## whenever the questions says numbers from 1 to n: think of cyclic sort no matter what
## like find the duplicate in sorted array of 1 to n, or smallest missing number like that


## array must have all elements in range(1,n)

'''
Cyclic sort: will sort the array in for loop

## when given numbers from 1 to n : use cyclic sort

since elements from 1 t n: so each nth element will be at (n-1) index in sorted array

in this we will start from the 0th index and will swap the element with the place it should be
We will continue this process after every swap 

So total comparisons in worst case: (n-1) + n == (2n-1) swaps in worst case
## time complexity : O(n)

(n-1) because it will keep on checking the 0th index with other elements
whether the oth index is 1 or not
and if 1: then will go on next index and will check for that also

'''

k = [1,2,3,6,5,4]

i=0
while i<len(k):
    correctIndex = k[i]-1
    if k[i] != k[correctIndex]:
        k[i],k[correctIndex] = k[correctIndex],k[i]
    else:
        i+=1    


print(k)

