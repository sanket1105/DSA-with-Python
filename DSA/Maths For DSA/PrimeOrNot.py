
## if 12*3 == 36
## no need to check 3 * 12 

### if you write all the factors of number, after its sqrt, the pattern of the factors returns
'''
1 * 36
2 * 18
3 * 12
4 * 9
6 * 6
9 * 4
12 *3 
18 * 2
36 * 1

## after 6 * 6, pattern is recurring
## so check till sqrt of the number
'''
import math
n = 119
ans = True
if n<2: ans=  False
else: 
    for i in range(2,int(math.sqrt(n))) :
        if n %i==0:
          ans = False
          break

if ans: print("Prime")
else: print("Not prime")    
