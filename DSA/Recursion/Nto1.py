

def Nto1(N):
    if N==1:
        print(1)
        return
    print(N)
    Nto1(N-1)

Nto1(5)

print("##########################################")

def OnetoN(N):
    if N==0:
        return
    OnetoN(N-1) 
    print(N)

OnetoN(5)
