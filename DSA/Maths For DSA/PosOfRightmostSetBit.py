
## negative of a number is 2's compliment

import math

def pos(n):
    if n==0: return 0
    return  int(math.log2(n & -n))+1


print(pos(1))
            

