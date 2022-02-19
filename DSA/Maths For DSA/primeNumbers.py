
## Brute force approach
'''
n = 100
for i in range(2,n+1):
    k = False
    for j in range(2,(i//2)+1):
        
        if i % j == 0 and i!=j:
            k = True
            break
    if k==False: print(i,end= " ")    


'''

## sieve of eratosthenes

def sieve(n):
    prime = [True] * (n+1)
    p = 2
    while p*p<=n:
        if prime[p] == True: ## if p is prime, then discard its multiples
            for i in range(p*2,n+1,p):  ## start form p+p that is 2*p
                prime[i] = False
        p += 1

    for i in  range(2,n+1):
        if prime[i] == True:
            print(i,end= " ")  

sieve(100)

