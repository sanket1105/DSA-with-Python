
## Also known as sinking sort and exchange sort and inplace sorting algo

'''
Its basically comparison sort method
In this first pass, the largest element comes in the end and so on....on each step

## no extra space used : O(1)
## time complexity : O(n**2)

In this the order after sorting is not maintained
just sorted according to the values and not the order of the elements

So bubble sort is the unstable algorithm.
'''

k = [2,2,1,1,1,2,2]

for i in range(len(k)):
    swap=False
    for j in range(1,len(k)-i):

        if k[j-1] > k[j]: ## swap
            k[j],k[j-1] = k[j-1],k[j]
            swap = True
    
    if swap==False:
        break

print(k)
print(swap)


