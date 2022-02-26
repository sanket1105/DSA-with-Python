

'''
Basic method is to find any number using for loops and all.
In this case, the time complexity is worst.

Now lets say the matrix is sorted row wise and column wise also.
So lets see the code
'''

## this matrix is not properly sorted
## sorted just row and column wise

a = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]
target = 55

r = 0
c = len(a[0])-1
found = False

while r<len(a) and c>=0:
    if a[r][c]==target:
        found = True
        print([r+1,c+1])
        break

    elif a[r][c] > target:
        c-=1
    else:
        r+=1

if found==False:
    print("index not found")





