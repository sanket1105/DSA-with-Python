
## this is the proper sorted matrix
## by using the previous method


'''
if you flatten the list, now: 1 2 3 4 5 6 7 8 9 10 11 12
int the list: 5 is at 4rd index

## now 4 in matrix is at [1,0] that is equal to : row_number*(number of cols) + col_number
that is 1*4+0 : 4 which is the index in the array

so row_number = array_index // number of cols
column_number = array_index % number of cols
'''

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
target = 12

m,n = len(a), len(a[0])
low=0
high = m*n -1
found=False

while low<=high:
    mid = (low+high)//2

    x,y = mid//n, mid%n
    if a[x][y] == target:
        found = True
        break

    elif a[x][y] < target:
        low = mid+1
    else: high = mid-1


if found==False: print("Not found")
else: print([x,y])




