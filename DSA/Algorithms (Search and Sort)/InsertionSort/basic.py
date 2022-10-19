

''''
Sorting the array partially.
that is firt sort till index 1 then index 2 then index 3 and so on.

So for every element,   its left side is sorted, so put the current index at its particular place in the LHS

## after every pass: left side is getting sorted

Worst case : O(n^2)
Best Case: O(n) : already sorted

Why insertion sort: Steps get reduced as a result, number of swaps get reduced as a result
## its stable
## use for smaller values for n
## works good when array is partially sorted

'''

k = [99,5,6,8,9,5,2,6,4,-1]

for i in range(len(k)-1):
    for j in range(i+1,0,-1):
        if k[j] < k[j-1]:
            k[j],k[j-1] = k[j-1],k[j]
        else:
            ## already sorted
            break
print(k)            