

def factors(n):
    ans = []
    for i in range(1,int((n**0.5))+1):
        if n%i==0:
            if i**2 == n:
                ans.append(i)
            else:
                ans.append(i)
                ans.append(n//i)

    print(sorted(ans))                

factors(20)            