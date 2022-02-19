

## more memory consumption

def Xpower(x,n):
    if n==0 or x==1: return 1
    return x*(Xpower(x,n-1))





## less memory consumption one

def XRaisedTOPower(x,n):
    if x==1 or n==0: return 1
    if x==0: return 0

    if(n%2==0): return XRaisedTOPower(x,int(n/2)) * XRaisedTOPower(x,int(n/2))
    else : return XRaisedTOPower(x,int(n/2)) * XRaisedTOPower(x,int(n/2)) * x


print(Xpower(3,0))  
print(XRaisedTOPower(3,3))  
print(XRaisedTOPower(5,3))  
