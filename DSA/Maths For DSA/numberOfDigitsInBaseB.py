
import math
def numberOfDigitsInBaseB(n,b):

    print( int(math.log2(n)/math.log2(b))+ 1)

numberOfDigitsInBaseB(32,2)




## draw the Pascal Triangle

def fact(n):
    if n<=1 : return 1
    return n * fact(n-1)
print("")
n = 7
for i in range(0,n+1):
    for j in range(0,i+1):
        ans = fact(i) / ((fact(j)) * fact(i-j))
        print(int(ans),end=" ")
    print("")    
