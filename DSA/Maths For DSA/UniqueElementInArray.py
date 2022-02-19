
def unique(arr):
    uni = 0
    for i in arr:
        uni = uni ^ i

    print(uni)

unique([1,2,3,4,3,2,1])


def ithBit(n,b):
    if n&(1<<(b-1)): print(1) ## if true
    else: print(0)

ithBit(10001,2)