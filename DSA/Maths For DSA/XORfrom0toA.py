
## 1 ^ 2 is 3
## write both in binary form and perform XOR on each bit

def XORfrom0toN(n):
    ## draw the XORs from 0 to a, and you will see the pattern
    arr = [n,1,n+1,0]
    return arr[n%4]

print(XORfrom0toN(4))