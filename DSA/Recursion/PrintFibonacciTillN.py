def fibo(a,b,n):
    if n==0: return 

    c = a+b
    print(c, end=" ")
    return fibo(b,c,n-1)


a,b = 0,1
print(a,end=" ")
print(b, end=" ")
n=10
fibo(a,b,n-2)