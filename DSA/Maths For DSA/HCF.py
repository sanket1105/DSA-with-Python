## Eucledian Algorithm

def hcf(a,b):
    if a==0: return b
    return hcf(b%a,a)


## LCM will be a*b / gcd(a,b)

def lcm(a,b):
    ans = a*b / (hcf(a,b))
    print(ans)

print(hcf(5,10))    
lcm(5,10)

