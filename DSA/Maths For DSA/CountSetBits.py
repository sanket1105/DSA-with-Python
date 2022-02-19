
## Normal Method
'''
def CountSetBits(n):

    count = 0
    while n:
        if n&1 == 1:
            count += 1
        n = n>>1
    print("Number of set bits: ",count)
'''

## best method 
## let us keep finding the right most bits in


def CountSetBits(n):
    count = 0
    while n>0:
        n = n - (n & -n)   ## deleting the right most number fromt the number table
        count += 1

    print(count)    

CountSetBits(45)


    