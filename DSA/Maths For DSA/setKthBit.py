
## set kth bit means:
## change the kth bit in the number to 1

## reset is just the opposite 
## if kth bit is 1: set as 0 
## ~ is not

def setKthBit(n,k):
    mask = 1 << (k-1)
    print(n | mask)

def resetkthBit(n,k):
    mask = (1<<(k-1))
    print( n & ~(mask))

  

setKthBit(5,2)
resetkthBit(7,3)